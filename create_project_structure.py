import os

# Define project structure
project_structure = {
    "notebooks": [
        "01_data_preparation.ipynb",
        "02_feature_engineering.ipynb",
        "03_model_training.ipynb",
        "04_model_evaluation.ipynb",
        "05_deployment.ipynb",
    ],
    "scripts": [
        "data_preparation.py",
        "feature_engineering.py",
        "model_training.py",
        "inference.py",
    ],
    "src/data": ["data_loader.py"],
    "src/features": ["feature_extractor.py"],
    "src/models": ["model.py", "train_utils.py", "evaluation.py"],
    "src/deployment": ["deploy.py"],
    "config": ["training_config.json", "model_config.json", "terraform_config.json"],
    "terraform": [
        "main.tf",
        "variables.tf",
        "outputs.tf",
        "provider.tf",
        "cloudwatch.tf",
    ],
    "tests": [
        "test_data_preparation.py",
        "test_feature_engineering.py",
        "test_model_training.py",
        "test_deployment.py",
    ],
    ".github/workflows": ["ci.yml"],
}

# Files in the root directory
root_files = [
    ".gitignore",
    "Dockerfile",
    "docker-compose.yml",
    "Jenkinsfile",
    "requirements.txt",
    "README.md",
]

# Function to create the project structure
def create_structure(base_path, structure, files):
    # Create root files
    for file in files:
        open(os.path.join(base_path, file), "w").close()

    # Create directories and files
    for folder, folder_files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        for file in folder_files:
            file_path = os.path.join(folder_path, file)
            open(file_path, "w").close()

# Generate the project structure
project_name = "malaria-classification-project"
os.makedirs(project_name, exist_ok=True)
create_structure(project_name, project_structure, root_files)

print(f"Project '{project_name}' structure created successfully!")