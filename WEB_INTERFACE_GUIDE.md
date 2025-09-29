# 🌐 Moot Court AI Web Interface Guide

## 🚀 **Interactive Web Platform**

Your Moot Court AI system now has a beautiful, interactive web interface built with Streamlit!

## 🎯 **Features**

### **🏠 Home Dashboard**
- System status overview
- Quick start guide
- Legal framework summary
- Navigation hub

### **⚖️ Case Argumentation**
- **Custom Case Input**: Enter your own case facts and legal issues
- **Example Cases**: 4 pre-loaded employment law scenarios
- **AI Argument Generation**: Professional legal arguments from all perspectives
- **Real-time Processing**: Progress indicators and status updates

### **📚 Legal Precedents Browser**
- **Search Functionality**: Find relevant cases by keywords
- **Relevance Scoring**: AI-powered similarity matching
- **Case Details**: Full text of legal precedents
- **Source Attribution**: Clear case citations

### **ℹ️ System Information**
- Technical specifications
- Legal framework details
- Usage instructions
- Support information

## 🎭 **Multi-Agent Argumentation**

### **👨‍💼 Claimant's Arguments**
- Procedural unfairness claims
- Substantive unfairness arguments
- Burden of proof analysis
- Specific relief sought
- Legal authority citations

### **🏢 Respondent's Defense**
- Procedural compliance arguments
- Valid grounds for dismissal
- Evidence presentation
- Reasonable employer test
- Cost submissions

### **⚖️ Judge's Decision**
- Legal framework analysis
- Procedural assessment
- Substantive evaluation
- Burden of proof determination
- Orders and relief

## 🚀 **How to Launch**

### **Method 1: Direct Streamlit Command**
```bash
# Activate virtual environment
source venv/bin/activate

# Launch the app
streamlit run moot_court_app.py
```

### **Method 2: Using the Launcher Script**
```bash
# Make script executable (if needed)
chmod +x run_app.py

# Run the launcher
python run_app.py
```

### **Method 3: Background Service**
```bash
# Run in background
streamlit run moot_court_app.py --server.port 8501 --server.headless true
```

## 🌐 **Access the Interface**

Once launched, the web interface will be available at:
- **Local URL**: http://localhost:8501
- **Network URL**: http://your-ip:8501 (for remote access)

## 📱 **Interface Layout**

### **Sidebar Navigation**
- 🏠 Home - Dashboard and overview
- ⚖️ Argue Case - Main case argumentation
- 📚 Browse Precedents - Legal database search
- ℹ️ About - System information

### **Main Content Area**
- **Case Input**: Text areas for facts and legal issues
- **Progress Indicators**: Real-time processing status
- **Results Display**: Tabbed interface for arguments
- **Metrics Dashboard**: System statistics

## 🎯 **Usage Workflow**

### **Step 1: Input Case**
1. Navigate to "Argue Case"
2. Choose input method (Custom or Example)
3. Enter case facts and legal issues
4. Click "Generate Legal Arguments"

### **Step 2: Review Arguments**
1. **Precedents Tab**: Review relevant legal cases
2. **Claimant Tab**: Read claimant's arguments
3. **Respondent Tab**: Review defense arguments
4. **Judge Tab**: See the judgment framework

### **Step 3: Research & Analysis**
1. Use "Browse Precedents" for additional research
2. Search for specific legal concepts
3. Review full case texts
4. Export or save results

## 🎨 **Visual Design**

### **Color Scheme**
- **Primary**: Professional blue (#1f4e79)
- **Claimant**: Green (#28a745) - Positive/Plaintiff
- **Respondent**: Red (#dc3545) - Defense/Defendant  
- **Judge**: Purple (#6f42c1) - Authority/Decision

### **Interactive Elements**
- **Progress Bars**: Real-time processing feedback
- **Expandable Cards**: Precedent details
- **Tabbed Interface**: Organized argument display
- **Status Indicators**: System health monitoring

## 🔧 **Technical Specifications**

### **Framework**
- **Frontend**: Streamlit 1.50.0
- **Backend**: Python 3.11
- **AI Models**: Hugging Face Transformers
- **Search**: FAISS vector database

### **Performance**
- **Response Time**: < 5 seconds per case
- **Concurrent Users**: Multiple sessions supported
- **Memory Usage**: Optimized for efficiency
- **Browser Compatibility**: Modern browsers supported

## 🛠️ **Customization Options**

### **Adding New Example Cases**
Edit the `load_example_cases()` function in `moot_court_app.py`:
```python
def load_example_cases():
    return [
        {
            "title": "Your Case Title",
            "facts": "Case facts here...",
            "issues": "Legal issues here..."
        }
        # Add more cases...
    ]
```

### **Modifying Styling**
Update the CSS in the `st.markdown()` section:
```python
st.markdown("""
<style>
    .your-custom-class {
        /* Your styles here */
    }
</style>
""", unsafe_allow_html=True)
```

### **Adding New Pages**
Create new page functions and add them to the sidebar selectbox:
```python
page = st.selectbox(
    "Choose a page:",
    ["🏠 Home", "⚖️ Argue Case", "📚 Browse Precedents", "🆕 Your New Page", "ℹ️ About"]
)
```

## 🚀 **Deployment Options**

### **Local Development**
- Perfect for testing and development
- Full access to all features
- Easy debugging and modification

### **Cloud Deployment**
- **Streamlit Cloud**: Free hosting for public repos
- **Heroku**: Easy deployment with git integration
- **AWS/GCP/Azure**: Scalable enterprise solutions

### **Production Considerations**
- **Security**: Add authentication if needed
- **Scaling**: Consider load balancing for high traffic
- **Monitoring**: Add logging and error tracking
- **Backup**: Regular data and model backups

## 🎉 **Ready to Use!**

Your Moot Court AI now has a professional, interactive web interface that makes legal argumentation accessible to anyone with a web browser. The system combines the power of AI with an intuitive user experience to deliver professional-quality legal analysis.

**Launch the interface and start arguing cases today!** ⚖️
