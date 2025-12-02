<h1>🚀 Career Guidance Multi-Agent System</h1>

<p>
<img src="https://img.shields.io/badge/AI-Career_Guide-blue" alt="AI Badge">
<img src="https://img.shields.io/badge/Python-3.10%2B-yellow" alt="Python Badge">
<img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Active Status Badge">
<img src="https://img.shields.io/badge/Google-ADK_Agents-red" alt="Google ADK Badge">
</p>

<h3>🎯 Short Description</h3>
<p>
An intelligent <strong>AI-driven multi-agent system</strong> designed to assist students and professionals in making smarter career choices. 
It provides personalized career paths, skill-building roadmaps, job market demand, and salary trend analysis — powered by 
<strong>Google ADK Agents</strong> and <strong>Gemini 2.5 Flash</strong>.
</p>

<hr>

<h2>🧠 Key Features</h2>
<ul>
    <li>Smart intent classification</li>
    <li>Profile-based career suggestions</li>
    <li>Roadmaps with skills, tools & certifications</li>
    <li>Job trends & market demand analysis</li>
    <li>Salary insights across regions 🌍</li>
    <li>Full pipeline mode: complete career report in one response</li>
    <li>Modular scalable multi-agent system</li>
</ul>

<hr>

<h2>🏗️ Architecture</h2>
<pre>
        ┌────────────────────────┐
        │      User Input        │
        └─────────────┬──────────┘
                      ▼
          ┌──────────────────────┐
          │  Classifier Agent    │
          └─────────────┬────────┘
                        ▼
 ┌──────────────────┬────────────┬───────────────────┐
 ▼                  ▼            ▼                   ▼
Profile Analyzer   Career Path   Roadmap Agent   Trends & Salary Agents
      Agent          Agent              │             (Job/Market/Salary)
       │                │               │                   │
       └────────────┬───┴──────────────┴───────────────────┘
                    ▼
          ┌──────────────────────┐
          │  Pipeline Agent      │
          │ (Final Report Gen.)  │
          └──────────────────────┘
</pre>

<hr>

<h2>🛠️ Tech Stack</h2>
<table border="1" cellspacing="0" cellpadding="5">
<tr><th>Component</th><th>Technology</th></tr>
<tr><td>Language</td><td>Python 3.10+</td></tr>
<tr><td>AI Model</td><td>Gemini 2.5 Flash</td></tr>
<tr><td>Framework</td><td>Google ADK Agents</td></tr>
<tr><td>Tools</td><td>Google Search Tool (internal)</td></tr>
</table>

<hr>

<h2>📦 Installation</h2>

<h3>🔑 Prerequisites</h3>
<ul>
    <li>Python 3.10+</li>
    <li>Google API Key (Gemini)</li>
</ul>

<h3>🧩 Setup</h3>
<pre>
git clone &lt;your-repository-url&gt;
cd &lt;project-folder&gt;

python -m venv venv
venv\Scripts\activate       # Windows
# or:
source venv/bin/activate    # macOS / Linux

pip install google-adk 
</pre>

<hr>

<h2>▶️ Usage</h2>
<pre>
adk web
</pre>

<hr>

<h2>📂 Folder Structure</h2>
<pre>
project/
│
├─ agent.py
└─ subagents/
    ├─ classifier/
    ├─ profileanalyze/
    ├─ careerpath/
    ├─ roadmap/
    ├─ jobtrends/
    ├─ salarytrend/
    ├─ markettrend/
    └─ pipeline/
</pre>

<hr>

<h2>🖼️ Screenshots / Demo</h2>
<p>📌 To be added later when UI is built</p>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
    <li>Resume analyzer + ATS scoring</li>
    <li>Personalized dashboards</li>
    <li>Real-time job API integration</li>
    <li>Skill gap analytics</li>
    <li>Multi-language support</li>
    <li>Web UI for public users</li>
</ul>

<hr>

<h2>👤 Author Info</h2>
<table border="1" cellspacing="0" cellpadding="5">
<tr><th>Info</th><th>Details</th></tr>
<tr><td>Name</td><td><strong>Soham Palkar</strong></td></tr>
<tr><td>LinkedIn</td><td><a href="https://www.linkedin.com/in/soham-palkar-a07058387/">Click Here</a></td></tr>
</table>

<hr>

<h2>📜 License</h2>
<p><em>Educational & Research Use Only</em> (License not openly provided yet)</p>

