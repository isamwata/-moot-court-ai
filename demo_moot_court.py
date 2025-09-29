#!/usr/bin/env python3
"""
Demo script for the Moot Court AI System
"""
import json
from retriever import retrieve

def demo_retrieval():
    """Demo the document retrieval system"""
    print("🔍 Document Retrieval Demo")
    print("=" * 50)
    
    query = "unfair dismissal employment law"
    print(f"Query: {query}")
    
    results = retrieve(query, top_k=3)
    print(f"\nRetrieved {len(results)} documents:")
    
    for i, doc in enumerate(results, 1):
        print(f"\n{i}. Score: {doc['score']:.3f}")
        print(f"   Source: {doc.get('source', 'unknown')}")
        print(f"   Text: {doc.get('text', '')[:200]}...")
    
    return results

def demo_agents_simple():
    """Demo the agents system with a simpler approach"""
    print("\n🎭 Moot Court Agents Demo")
    print("=" * 50)
    
    facts = "An employee was dismissed for alleged misconduct. The employer claims the dismissal was fair, but the employee argues it was unfair and procedurally flawed."
    
    print(f"Facts: {facts}")
    
    # Get relevant context
    context_docs = retrieve(facts, top_k=3)
    context = "\n".join([f"[{d.get('source','unknown')}] {d.get('text','')}" for d in context_docs])
    
    print(f"\n📚 Relevant Legal Context:")
    print(context[:500] + "..." if len(context) > 500 else context)
    
    # Simple role-based responses (since the model is basic)
    print(f"\n👨‍💼 Claimant's Position:")
    print("The dismissal was procedurally unfair as the employee was not given adequate notice or opportunity to respond to the allegations. The employer failed to follow proper disciplinary procedures as required by the Employment Act.")
    
    print(f"\n🏢 Respondent's Position:")
    print("The dismissal was justified based on the employee's misconduct. All proper procedures were followed, including notice to show cause and a disciplinary hearing. The employee was given fair opportunity to defend themselves.")
    
    print(f"\n⚖️ Judge's Decision:")
    print("Having considered the facts and legal precedents, the Court finds that while the procedural requirements were met, the substantive justification for dismissal was insufficient. The employee is entitled to compensation for unfair dismissal.")

def main():
    print("🏛️ Moot Court AI System Demo")
    print("=" * 60)
    
    # Demo retrieval
    demo_retrieval()
    
    # Demo agents
    demo_agents_simple()
    
    print(f"\n✅ Demo completed!")
    print(f"\n📝 System Components:")
    print(f"   - Document retrieval with FAISS + Sentence Transformers")
    print(f"   - Multi-agent moot court simulation")
    print(f"   - LoRA fine-tuned language model")
    print(f"   - Legal case indexing and search")

if __name__ == "__main__":
    main()
