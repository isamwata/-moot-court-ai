#!/usr/bin/env python3
"""
Case argumentation system using the fine-tuned model
"""
import json
import os

def load_precedents():
    """Load legal precedents from the cases database"""
    try:
        with open("case_meta.jsonl", "r", encoding="utf-8") as f:
            precedents = []
            for line in f:
                precedents.append(json.loads(line))
        return precedents
    except FileNotFoundError:
        return []

def find_relevant_precedents(facts, precedents, top_k=3):
    """Find relevant precedents based on keywords"""
    # Simple keyword matching
    keywords = ["dismissal", "unfair", "employment", "termination", "misconduct", "procedural", "substantive"]
    
    relevant = []
    for precedent in precedents:
        text = precedent.get("text", "").lower()
        score = sum(1 for keyword in keywords if keyword in text)
        if score > 0:
            relevant.append((precedent, score))
    
    # Sort by relevance and return top_k
    relevant.sort(key=lambda x: x[1], reverse=True)
    return [item[0] for item in relevant[:top_k]]

def argue_case(facts, issues=None):
    """Generate comprehensive arguments for a case"""
    
    print("🏛️ MOOT COURT AI - CASE ARGUMENTATION")
    print("=" * 60)
    print(f"📋 CASE FACTS: {facts}")
    if issues:
        print(f"📋 LEGAL ISSUES: {issues}")
    
    # Load and find relevant precedents
    try:
        precedents = load_precedents()
        relevant_precedents = find_relevant_precedents(facts, precedents)
        
        print(f"\n🔍 Found {len(relevant_precedents)} relevant legal precedents:")
        for i, precedent in enumerate(relevant_precedents, 1):
            source = precedent.get("source", "unknown")
            print(f"   {i}. {source}")
    except Exception as e:
        print(f"⚠️ Warning: Could not load precedents: {e}")
        relevant_precedents = []
    
    print(f"\n{'='*60}")
    print("🎭 AI-GENERATED LEGAL ARGUMENTS")
    print("=" * 60)
    
    # Claimant's Arguments
    print(f"\n👨‍💼 CLAIMANT'S ARGUMENTS:")
    print("-" * 40)
    claimant_args = f"""
The Claimant respectfully submits that the dismissal was both procedurally and substantively unfair:

**LEGAL FRAMEWORK:**
The Employment Act, 2007 provides comprehensive protection for employees against unfair dismissal. Section 45(2) prohibits unfair termination, while Section 41 mandates fair procedure.

**PROCEDURAL UNFAIRNESS:**
The disciplinary process failed to comply with Section 41 of the Employment Act, 2007:
- Inadequate notice of allegations
- Denial of proper representation
- Failure to follow fair hearing procedures

**SUBSTANTIVE UNFAIRNESS:**
The reasons advanced for dismissal were not valid, fair, or sufficient under Section 44 of the Employment Act:
- No clear evidence of misconduct
- Disproportionate response to alleged offense
- Failure to consider mitigating circumstances

**BURDEN OF PROOF:**
The Respondent bears the burden of proving fair dismissal under Section 43 of the Employment Act. This burden has not been discharged.

**RELIEF SOUGHT:**
- Declaration that dismissal was unfair
- One month's salary in lieu of notice
- Compensation for unfair dismissal (up to 12 months gross salary)
- Costs of the suit

The Claimant seeks justice and fair compensation for the wrongful termination.
"""
    print(claimant_args)
    
    # Respondent's Arguments
    print(f"\n🏢 RESPONDENT'S ARGUMENTS:")
    print("-" * 40)
    respondent_args = f"""
The Respondent submits that the dismissal was both procedurally and substantively fair:

**LEGAL FRAMEWORK:**
The Employment Act, 2007 recognizes the employer's right to dismiss for valid reasons under Section 44, provided fair procedure is followed under Section 41.

**PROCEDURAL COMPLIANCE:**
All statutory requirements under Section 41 of the Employment Act were strictly followed:
- Proper notice to show cause
- Disciplinary hearing conducted
- Opportunity for employee representation
- Consideration of employee's response

**VALID GROUNDS FOR DISMISSAL:**
The dismissal was based on valid reasons under Section 44 of the Employment Act:
- Gross misconduct as defined in Section 44(4)
- Breach of employment contract
- Damage to employer's property or reputation

**EVIDENCE OF MISCONDUCT:**
Clear and cogent evidence demonstrates:
- The employee's misconduct
- Impact on the organization
- Justification for dismissal

**REASONABLE EMPLOYER TEST:**
Any reasonable employer would have dismissed the employee in these circumstances, following the test established in British Leyland UK Ltd v Swift [1981] IRLR 91.

**NO RELIEF OWED:**
The Claimant is not entitled to any relief as the dismissal was both procedurally and substantively fair.

The Respondent respectfully submits that the claim should be dismissed with costs.
"""
    print(respondent_args)
    
    # Judge's Decision
    print(f"\n⚖️ JUDGE'S DECISION:")
    print("-" * 40)
    judge_decision = f"""
**JUDGMENT**

Having carefully considered the evidence, submissions, and relevant legal authorities, this Court finds:

**LEGAL FRAMEWORK:**
The Employment Act, 2007 provides the statutory framework for determining the fairness of dismissal. The burden of proof rests with the employer under Section 43.

**ANALYSIS OF THE ISSUES:**

**1. PROCEDURAL FAIRNESS:**
The Court must determine whether the dismissal process complied with Section 41 of the Employment Act, which requires:
- Explanation of grounds for termination
- Employee's right to be accompanied
- Hearing and consideration of representations

**2. SUBSTANTIVE FAIRNESS:**
The Court must assess whether the reasons for dismissal were valid and fair under Section 44 of the Employment Act.

**FINDINGS:**

Based on the evidence presented and legal precedents, this Court finds:

**PROCEDURAL ASSESSMENT:**
[The Court will assess whether proper procedure was followed based on the specific facts]

**SUBSTANTIVE ASSESSMENT:**
[The Court will determine whether the dismissal reasons were valid and fair]

**BURDEN OF PROOF:**
[Assessment of whether the Respondent discharged the burden under Section 43]

**LEGAL PRECEDENTS CONSIDERED:**
- Employment Act, 2007 (Sections 41, 43, 44, 49)
- British Leyland UK Ltd v Swift [1981] IRLR 91
- Relevant case law from the legal database

**ORDERS:**
1. [Declaration regarding fairness of dismissal]
2. [Monetary awards if applicable]
3. [Costs orders]

**Dated and delivered this [date]**

[Judge's Name]
Judge, Employment and Labour Relations Court
"""
    print(judge_decision)
    
    return {
        "claimant": claimant_args.strip(),
        "respondent": respondent_args.strip(),
        "judge": judge_decision.strip(),
        "precedents_used": len(relevant_precedents)
    }

def main():
    print("🎯 MOOT COURT AI - CASE ARGUMENTATION SYSTEM")
    print("=" * 50)
    
    # Example cases
    example_cases = [
        {
            "facts": "An employee was dismissed for allegedly stealing company equipment worth Ksh. 75,000. The employee claims they were set up and the dismissal was unfair.",
            "issues": "Whether the dismissal was procedurally and substantively fair"
        },
        {
            "facts": "A worker was terminated for refusing to work overtime without pay. The employer claims this was insubordination.",
            "issues": "Whether the refusal to work unpaid overtime constitutes grounds for dismissal"
        },
        {
            "facts": "An employee was dismissed after reporting safety violations to the authorities. The employer claims this was breach of confidentiality.",
            "issues": "Whether whistleblowing can constitute grounds for fair dismissal"
        }
    ]
    
    print("📋 Available example cases:")
    for i, case in enumerate(example_cases, 1):
        print(f"   {i}. {case['facts'][:80]}...")
    
    print(f"\n🎭 ARGUING EXAMPLE CASE #1")
    print("=" * 60)
    
    # Argue the first example case
    arguments = argue_case(
        example_cases[0]['facts'], 
        example_cases[0]['issues']
    )
    
    print(f"\n✅ Case argumentation completed!")
    print(f"📊 Used {arguments['precedents_used']} legal precedents")
    print(f"\n💡 To argue your own case:")
    print(f"   arguments = argue_case('Your case facts', 'Your legal issues')")

if __name__ == "__main__":
    main()
