## Husak.University.Google-Calendar (Project - 6)
## Author
Mariia Husak FEP-21

husakmaria74@gmail.com

https://t.me/@gusakmary
## Getting Started
#### To run project locally, follow next steps:

Clone the repository: ``` git clone https://github.com/MariaHusak/Husak.University.Google-Calendar.git ```

Install dependencies: ``` pip install -r requirements.txt ```

Run the development server: ``` python manage.py runserver ```

### Getting Started with Local Setup for Google Calendar
Welcome to Google Calendar! This guide will walk you through the process of setting up Google Calendar locally on your computer.
#### Prerequisites
Before you begin, ensure you have the following:
- A Google account
- A computer with internet access
- A web browser (Google Chrome, Mozilla Firefox, Safari, etc.)
#### Table of Contents
- Creating Events
- Managing Invitations
- Privacy Policy

#### Step 1: Creating Events
##### Using the Calendar Interface
1. Learn how to navigate the calendar interface.
2. Access different views such as daily, weekly, and monthly.

##### Adding Events
1. Click on a date to create a new event.
2. Fill in event details such as title, date, time, location, and description.
3. Optionally set recurrence patterns for recurring events.
 
##### Editing Events
1. Edit event details directly from the calendar interface.
2. Change event time, location, or description as needed.

#### Step 2: Managing Invitations
##### Receiving Invitations
1. Understand how to receive event invitations from other users.
2. Get notified via email when you receive a new invitation.
   
##### Responding to Invitations
1. Accept or decline event invitations directly from your calendar interface.
2. RSVP to invitations to let organizers know your availability.

#### Step 3: Privacy Policy
##### Information Collection
1. Learn about the types of information collected when using Google Calendar.
2. Understand how your personal data is handled and protected.
   
##### Data Usage
1. Explore how collected information is used to provide the calendar service.
2. Discover how event data is processed and stored securely.

##### User Control and Rights
1. Learn about your rights regarding access, update, and deletion of account and event data.
2. Understand how to control notifications and opt-out of certain data processing activities.

#### Conclusion
You're now ready to start using Google Calendar to manage your events and stay organized. If you have any questions or need further assistance, feel free to explore the help resources provided by Google or reach out to their support team.

Happy scheduling! 🗓️

## Project Documentation
### Introduction
Welcome to the documentation for project, a comprehensive and user-friendly calendar application built on the Django framework. This documentation serves as a guide for developers, testers providing insights into its architecture, features, deployment process, and more.
### Architecture Diagram 
You can see the architecture diagram here:

https://miro.com/app/board/uXjVKNOG358=/
### Infrastructure Diagram
You can see the infrastructure diagram here:

https://miro.com/app/board/uXjVKb2V8W0=/

### Azure deployment process
##### 1. Prepare Django Application
Ensure that your Django application is properly configured and works correctly on your local development machine. Make sure all dependencies are listed in requirements.txt or Pipfile, and your application can run using python manage.py runserver without any errors.

##### 2. Set Up Azure Account
If you haven't already, sign up for an account on Azure. You may need to provide payment information, but Azure often offers free trials and credits for new users.

##### 3. Deploy to Azure App Service
Assuming you choose Azure App Service:

Install the Azure CLI on your local machine if you haven't already.
Log in to Azure CLI using az login command.
Navigate to your Django project directory.
Run az webapp up --sku F1 --name <your-app-name> to deploy your Django application to Azure App Service. Replace <your-app-name> with a unique name for your application.
Azure CLI will guide you through the deployment process and provide a URL where your application will be accessible.

##### 4. Configure Environment Variables
Ensure that your Django application's environment variables, such as database credentials and secret keys, are properly configured on Azure App Service. You can set them using Azure Portal or Azure CLI.

##### 5. Set Up Database
If you're using a database with your Django application, set up the database on Azure. Azure offers managed database services like Azure Database for PostgreSQL or Azure Database for MySQL.

##### 6. Configure Static Files and Media Storage
For static files and media storage, consider using Azure Blob Storage or Azure CDN (Content Delivery Network) to serve static assets efficiently.

##### 7. Set Up SSL/TLS Certificates
Enable HTTPS for your Django application to ensure secure communication. You can use Azure's built-in support for SSL/TLS certificates or bring your own certificate.

##### 8. Test Application
Once deployed, thoroughly test your Django application on Azure to ensure everything works as expected. Check for any configuration issues, performance bottlenecks, or compatibility problems.

##### 9. Monitor and Maintain
Monitor your application's performance and resource usage on Azure. Use Azure's monitoring tools to identify and address any issues promptly. Regularly update your application and dependencies to keep it secure and up-to-date.

### Continuous Integration/Continuous Deployment (CI/CD) Process Documentation
#### Introduction:
Continuous Integration/Continuous Deployment (CI/CD) is a software development practice aimed at delivering code changes more frequently and reliably. It involves automating the process of integrating code changes into a shared repository (Continuous Integration) and deploying applications to production environments automatically (Continuous Deployment). This documentation outlines the CI/CD process implemented within our organization.

#### 1. Purpose:
The purpose of this document is to provide a comprehensive guide to the CI/CD process followed. It includes an overview of the process, its benefits, and step-by-step instructions for developers and operations teams to understand and utilize the CI/CD pipeline effectively.

#### 2. Overview:
The CI/CD process involves the following key stages:

##### Version Control:
Developers work on code changes in feature branches within a version control system (e.g., Git).

##### Continuous Integration (CI): 
Code changes are automatically merged into a shared repository multiple times a day. Automated tests are executed to ensure that the new changes do not introduce any regressions.

##### Continuous Deployment (CD):
Once the changes pass all tests in the CI stage, they are automatically deployed to staging or production environments.
#### 3. Benefits:
Implementing CI/CD offers several benefits, including:

##### Faster Time-to-Market:
Automating the build, test, and deployment processes speeds up the delivery of new features and bug fixes.

##### Higher Quality: 
Automated testing helps catch bugs early in the development process, ensuring a higher quality of code.

##### Improved Collaboration:
CI/CD encourages collaboration among developers, testers, and operations teams by providing a standardized and automated process.
#### 4. CI/CD Process:
The CI/CD process consists of the following steps:

##### Code Development:
Developers work on code changes in feature branches.

##### Code Review:
Pull requests are created for code changes, and peer reviews are conducted to ensure code quality and adherence to coding standards.

##### Continuous Integration (CI):

Trigger: Whenever a pull request is merged into the main branch or when changes are pushed to feature branches.

Actions:


Automated build: The code is compiled and built into executable artifacts.

Automated tests: Unit tests, integration tests, and other types of tests are executed to verify the correctness of the code changes.

Static code analysis: Tools such as linters and code quality analyzers are used to check for coding standards and potential issues.

Code coverage analysis: Assess the percentage of code covered by automated tests.

Notifications: Notify developers of the CI pipeline status (success or failure) via messaging platforms or email.

##### Continuous Deployment (CD):

Trigger: After successful completion of the CI stage.

Actions:


Artifact deployment: Deploy the built artifacts to staging environments for further testing.

Automated acceptance testing: Execute automated tests in the staging environment to ensure that the application behaves as expected.

Manual testing (optional): If necessary, perform manual testing in the staging environment.

Deployment to production: Upon successful testing in the staging environment, automatically deploy the changes to production environments.

Notifications: Notify stakeholders of deployment status and any issues encountered during the deployment process.

#### 5. Tools and Technologies:
The following tools and technologies are commonly used in our CI/CD process:

Version Control: Git

CI/CD Pipeline: Jenkins, GitLab CI/CD, Travis CI

Automated Testing: JUnit, Selenium, Jest, pytest

Artifact Repository: Nexus, Artifactory

Deployment Tools: Ansible, Docker, Kubernetes

Monitoring: Prometheus, Grafana

### Feedback
We value your feedback and strive to continuously improve Google Calendar. If you have any suggestions, feature requests, or bug reports, please don't hesitate to reach out to us. Your input helps us make Google Calendar better for everyone.

#### How to Provide Feedback
There are several ways you can provide feedback:

##### 1. GitHub Issues:
Submit an issue on GitHub with a clear description of your feedback. Whether it's a bug you encountered, a feature you'd like to see, or a suggestion for improvement, we appreciate hearing from you.

##### 2. Feature Requests:
If there's a feature you'd like to see added to Google Calendar, please let us know! Describe the feature in detail and explain how it would benefit you and other users.

##### 3. Bug Reports: 
Encountered a bug while using Google Calendar? Please report it so we can investigate and fix it promptly. Be sure to include steps to reproduce the bug and any error messages you encountered.

##### 4. General Suggestions: 
Have a general suggestion for improving Google Calendar? We're all ears! Whether it's usability improvements, design enhancements, or performance optimizations, your ideas are valuable to us.

#### What to Expect
##### -Timely Response: 
We aim to respond to feedback and bug reports as quickly as possible. Please be patient as we investigate and address your concerns.

##### -Transparency: 
We'll keep you informed about the status of your feedback. Once a bug is fixed or a feature is implemented, we'll update you on the progress.

##### -Community Engagement: 
Your feedback helps shape the future of Google Calendar. We encourage community members to engage in discussions, share their thoughts, and collaborate on making Google Calendar even better.

#### Thank You!
Thank you for taking the time to provide feedback on Google Calendar. Your input is invaluable to us and helps us create a more robust and user-friendly application for everyone.

## Project Task Decomposition
#### 1. Project Planning and Setup:
Define project scope, objectives, and deliverables.

Set up project repository on GitHub.

Define project structure and directory layout.

Set up virtual environment and install necessary dependencies.

#### 2. Frontend Development:
Design wireframes and user interface mockups.

Implement HTML/CSS templates for different pages (e.g., homepage, calendar view, event details).

Implement frontend logic using JavaScript.

#### 3. Backend Development:
Define data models for users, events, calendars, etc.

Implement authentication and authorization mechanisms.

Implement CRUD (Create, Read, Update, Delete) operations for managing events, calendars, etc.

Implement business logic for handling calendar events, reminders, notifications, etc.

#### 4. Database Setup and Management:
Choose a suitable database (e.g., MySQL).

Set up database schema based on defined data models.

Implement database migrations for version control of database schema changes.

#### 5. Deployment and Infrastructure Setup:
Choose a suitable hosting provider (e.g., Azure).

Set up deployment pipelines for continuous integration and deployment (CI/CD).

Configure server environment and dependencies.

Deploy application to production server.

#### 6. Documentation and Knowledge Sharing:
Write project documentation including setup instructions, API documentation, and user guides.

Create architecture diagrams and infrastructure diagrams for better understanding of system components.

Document CI/CD processes and best practices for future reference.

### Week 1:
- Implement feature: User authentication with Google Account (OAuth 2.0) ✔️
- Set up Azure deployment environment ✔️ 
- Create project structure on GitHub repository ✔️ 
- Define initial project architecture ✔️ 
- Write Getting Started documentation for local setup ✔️

### Week 2:
- Implement feature: Calendar View with Monthly Layout ✔️
- Set up Continuous Integration/Continuous Delivery (CI/CD) pipeline  ✔️
- Write Project Documentation: Architecture Diagram ✔️
- Write Unit Tests for User Authentication ✔️ 
- Create Postman collection for testing OAuth endpoints

### Week 3:
- Implement feature: Event Creation functionality ✔️ 
- Configure Azure deployment settings
- Write Project Documentation: Infrastructure Diagram ✔️ 
- Write Unit Tests for Event Creation functionality ✔️ 
- Write documentation for Azure deployment process ✔️ 

### Week 4:
- Implement feature: Reminder Notifications via Email  ✔️ 
- Implement automated deployment using CI/CD pipeline ✔️
- Write Project Tasks Decomposition ✔️
- Write Unit Tests for Reminder Notifications ✔️ 
- Create Postman collection for testing Reminder endpoints

### Week 5:
- Implement feature: Invite Attendees to Events ✔️
- Optimize Azure deployment for performance
- Write documentation for CI/CD process ✔️
- Write Unit Tests for Invite Attendees functionality ✔️
- Conduct unit testing for OAuth endpoints ✔️

### Week 6:
- Implement feature: Recurring Events ✔️
- Perform load testing on Azure deployment
- Update Project Documentation based on feedback ✔️
- Write Unit Tests for Recurring Events ✔️
- Conduct unit testing for Event Creation endpoints ✔️

### Week 7:
- Implement feature: Event Editing ✔️
- Design UI for Event Editing ✔️
- Review and refine Project Tasks Decomposition  ✔️
- Write Unit Tests for Event Editing ✔️
- Conduct unit testing for Reminder endpoints ✔️

### Week 8:
- Implement feature: Guest RSVP for Events ✔️
- Develop UI components for Event Creation ✔️
- Review and refine documentation ✔️
- Write Unit Tests for Guest RSVP functionality ✔️
- Conduct unit testing for Invite Attendees endpoints ✔️

### Week 9:
- Implement feature: Sharing Calendars ✔️
- Design UI components for displaying Calendar View ✔️
- Address any outstanding issues in documentation ✔️
- Write Unit Tests for Sharing Calendars ✔️
- Conduct unit testing for Recurring Events endpoints ✔️

### Week 10:
- Implement feature: Search Functionality ✔️
- Conduct user acceptance testing (UAT) +-
- Finalize documentation for release ✔️
- Write Unit Tests for Search Functionality ✔️
- Conduct unit testing for Event Editing endpoints ✔️

### Week 11:
- Implement feature: Customizable Event Categories
- Prepare for project deployment
- Conduct final round of testing and bug fixes
- Write Unit Tests for Customizable Event Categories
- Conduct unit testing for Guest RSVP endpoints

### Week 12:
- Implement feature: Welcome Email
- Finalize deployment and release
- Conduct post-release monitoring and support
- Conduct retrospective meeting for project review
- Write Unit Tests for remaining functionalities
- Conduct unit testing for Sharing Calendars endpoints
