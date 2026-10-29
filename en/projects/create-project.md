# Create Project

## Creating and Managing a Project

Projects help you group resources and control who can access them. This guide explains how to create a project in UzCloud, add users to it, and set quotas for the project.

### Creating a New Project

- In the left-hand menu, click **Projects**. The page shows all your projects.
- Click **+ Create New Project**.

![Projects](../../images/create-project.png)

- Enter the **Project Name** and **Project Description** (up to 250 characters) and select the **Project Purpose**. Optionally, change the project icon by clicking the pencil on the image.
- Click **Create Project**.

![Create Project](../../images/create-new-project.png)

### View Project Resources

To open a project, click **VIEW** on its card. The project page shows the number of resources in the project: **Instances**, **Instances Snapshot**, **Backups**, **Network**, **Load Balancer** and **Kubernetes**. To edit the project name and description, click the pencil icon in the top-right corner.

![Project Resources](../../images/create-new-project-resources.png)

### Adding Users to a Project

- In the **Users In Project** block, click **+ Add users to the project**.
- Use the search bar to find users, select them with the checkboxes, and click **Assign**.
- If the user does not exist yet, click **+ Create new user**.

![Add Users to the Project](../../images/create-new-project-add-user.png)

### Setting Quotas for a Project

The **Project Quota Limit** block shows the limit and usage of each resource in the project for the selected zone.

- Select the zone in **Select Zone**.

![Project Quota Limit](../../images/create-new-project-account-limit.png)

- Click **Edit Quota Limit**. The **Assign a quota to the project** window opens.
- Select the zone and enter the **Quota Limit** for the resources you want to limit. The value `-1` means an **unlimited** quota.
- Click **Submit**.

![Assign a Quota to the Project](../../images/create-new-project-account-limit-increase.png)

By following this guide, you can create and manage projects in UzCloud, organize team access, and control resource consumption.
