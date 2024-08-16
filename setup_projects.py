import os

# Define the root directory (this will be your repository root)
root_dir = "Finance-Projects"

# List of project names (add more as needed)
projects = [
    "Project_Template",
    "Project_Adam_Smith",  # Updated project name
    "Project_Beta_Analysis",
    "Project_Risk_Profiler",
    "Project_Personalized_Portfolio",
    "Project_Strategic_Asset_Allocation",
    "Project_ESG_Screener",
    "Project_Liquidity_Analysis",
    "Project_Alpha_Generation",
    "Project_Macro_Economic_Analysis",
    "Project_Time_Series_Forecasting",
    "Project_Credit_Risk",
    "Project_Tax_Efficiency",
    "Project_Volatility_Modeling",
    "Project_FX_RiskManagement",
    "Project_Market_Neutral_Strategy",
    "Project_Derivatives_Valuation",
    "Project_Private_Equity_Valuation",
    "Project_Alternative_Investments",
    "Project_Smart_Beta_Strategy",
    "Project_Sentiment_Analysis",
    "Project_Client_Reporting_Automation",
    "Project_Investment_Policy_Statement"
]

# Standard folders within each project
standard_folders = ["data", "notebooks", "scripts", "results"]

# Create the root directory
if not os.path.exists(root_dir):
    os.makedirs(root_dir)

# Loop through each project and create the folder structure
for project in projects:
    project_path = os.path.join(root_dir, project)
    
    # Create the main project directory
    if not os.path.exists(project_path):
        os.makedirs(project_path)
    
    # Create the standard subfolders
    for folder in standard_folders:
        folder_path = os.path.join(project_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    

    # Create the requirements.txt file as a placeholder
    requirements_path = os.path.join(project_path, "requirements.txt")
    with open(requirements_path, "w") as requirements_file:
        requirements_file.write("# Add project-specific dependencies here.\n")

print(f"Project folders and files have been created under the '{root_dir}' directory.")
