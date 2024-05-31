React Project Setup Script
This script automates the initial setup process for a React project, including the creation of environment variable files, configuration files, directory structure, and installation of dependencies.

Instructions
Clone Repository:
Clone this repository to your local machine:

bash
git clone <repository-url>
Navigate to Project Directory:
Change directory to the cloned repository:

bash
cd <repository-directory>
Run Setup Script:
Run the setup script:

bash
./setup_env.sh
This script will perform the following actions:

Create environment variable files .env.uat and .env.prod.
Create Prettier configuration file .prettierrc.
Create TypeScript configuration files tsconfig.json and tsconfig.node.json.
Create Vite configuration file vite.config.ts.
Install necessary dev dependencies: Prettier, ESLint, env-cmd, and Vite plugins.
Add scripts to package.json for development and production environments.
Create directory structure inside src directory.
Create src/app/store.ts file.
Verify Files and Directory Structure:
After running the script, verify the following:

Check for .env.uat, .env.prod, .prettierrc, tsconfig.json, tsconfig.node.json, and vite.config.ts files in the root directory.
Check the directory structure inside the src directory for the specified folders.
Open src/app/store.ts file to ensure it's created with the specified content.
Start Development Server:
Once the setup is complete, you can start the development server using one of the following commands:

bash
npm run dev:uat   # Start development server with UAT environment
npm run dev:prod  # Start development server with production environment
Build for Deployment:
To build the project for deployment, use one of the following commands:

bash
npm run build:uat   # Build project for UAT environment
npm run build:prod  # Build project for production environment
