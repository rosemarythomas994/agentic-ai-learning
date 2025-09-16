## **HR-ASSIST Agentic AI System**
---
HR ASSIST is an Agentic AI system designed to help HR teams automate routine workflows. This example demonstrates automation of the employee onboarding process, streamlining tasks that 
typically require manual intervention.

In terms of technical architecture, for MCP client we use Claude Desktop and the code base here represents the MCP server with necessary tools that will be used by MCP client 

🛠️ Setup Instructions

To set up and run HR ASSIST, follow these steps:

- Configure claude_desktop_config.json
Add the following configuration to your claude_desktop_config.json file:

    ```json
    {
    "mcpServers": {
        "hr-assist": {
        "command": "C:\\Users\\dhaval\\.local\\bin\\uv",
        "args": [
            "--directory",
            "C::\\code\\atliq-hr-assist",
            "run",
            "server.py"
        ],
        "env": {
            "CB_EMAIL": "YOUR_EMAIL",
            "CB_EMAIL_PWD": "YOUR_APP_PASSWORD"
        }
        }
    }
    }
    ```

- Replace YOUR_EMAIL with your actual email.
- Replace YOUR_APP_PASSWORD with your email provider’s app-specific password (e.g., for Gmail).
- Run `uv init` and `uv add mcp[cli]` as per the video tutorial in the course.  

**Usage**
- Click on the `+` icon and select the `Add from hr-assist` option, and send the request.
- Fill the details for the new employee:

<img src="resources\image.jpg" alt="Claude desktop prompt with fields" style="width:auto;height:300px;padding-left:30px">

Alternatively, you can draft a custom prompt and let the agent take over.


All rights reserver @Codebasics Inc and LearnerX India Private Ltd.


The HR-ASSIST Agentic AI System is an autonomous AI-powered tool created to help HR teams automate routine tasks, specifically demonstrated here for the employee onboarding process. Instead of manually handling repetitive onboarding steps, this system streamlines and automates those workflows, saving time and reducing errors.

Key Components and Architecture
The system involves two main parts:

The MCP client, which users interact with, is based on Claude Desktop (an AI-enabled desktop platform).

The MCP server contains the core codebase and tools required to handle the actual processing and workflow automation related to HR tasks like onboarding.

Setup Instructions
To get HR ASSIST running, configure the file claude_desktop_config.json with server details under "mcpServers".

The "hr-assist" server configuration specifies:

The command and arguments to run the server code (server.py) located in the directory C::\code\atliq-hr-assist.

Environment variables include the user’s email and an app-specific password (needed for authentication, such as with Gmail).

After configuring, run commands uv init and uv add mcp[cli] to initialize and add necessary server components following a tutorial.

How to Use
On the Claude Desktop interface:

Click the + icon and select Add from hr-assist.

The system will prompt for details of the new employee.

You can fill in these fields directly, or alternatively, draft a custom prompt where the AI agent will handle the onboarding tasks autonomously.

Summary
HR-ASSIST leverages agentic AI via the Claude Desktop and a backend MCP server to automate the employee onboarding workflow in HR departments. The setup involves configuring connection details and credentials, then using the AI client interface to send requests and enter employee data, allowing the agent to manage subsequent actions automatically.