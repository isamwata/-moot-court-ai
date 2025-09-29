#!/usr/bin/env python3
"""
Simple launcher script for the Moot Court AI Streamlit app
"""
import subprocess
import sys
import os

def main():
    """Launch the Streamlit app"""
    print("🏛️ Starting Moot Court AI Web Interface...")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("moot_court_app.py"):
        print("❌ Error: moot_court_app.py not found in current directory")
        print("Please run this script from the project root directory")
        sys.exit(1)
    
    # Check if virtual environment exists
    if not os.path.exists("venv"):
        print("❌ Error: Virtual environment not found")
        print("Please ensure the virtual environment is set up")
        sys.exit(1)
    
    print("✅ All checks passed")
    print("🚀 Launching Streamlit app...")
    print()
    print("📱 The app will open in your browser at: http://localhost:8501")
    print("🛑 Press Ctrl+C to stop the server")
    print()
    
    try:
        # Launch Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "moot_court_app.py",
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
    except KeyboardInterrupt:
        print("\n🛑 Server stopped by user")
    except Exception as e:
        print(f"❌ Error launching app: {e}")

if __name__ == "__main__":
    main()
