# Create Auto Scaling

## Auto-scaling

**Auto-scaling** is a cloud computing feature that automatically adjusts the number of virtual machine (VM) instances in response to real-time demand. It ensures that your applications remain available and perform optimally while minimizing costs by scaling resources up or down based on usage.

---

### Creating Auto-scaling

- From the left-hand side menu, click on the **Auto-scaling** tab.
- To create an auto-scaling group, click the **Auto-scaling** or **Create New** icon located on the right side of the page. This will open the auto-scaling creation menu.

![Auto Scaling](../../images/as-1.png)

### Assign to a Project

- Assign the auto-scaling group to one of your projects to organize and manage resources effectively.

![Auto Scaling](../../images/as-2.png)

### Choose a Location

- Select the data center location where your server will be physically hosted.
- Choose from the available locations listed.

![Auto Scaling](../../images/as-3.png)

### Choose Network

- Set up or choose a network for your server. This can be an isolated private network, or you can create an elastic network to connect multiple regions.
- Alternatively, you can also create or set up a new network by selecting **Create New Network**.

![Auto Scaling](../../images/as-4.png)

### Select Load Balancer

- A load balancer distributes incoming traffic across multiple VM instances. Select the **Load Balancer** you want from the available list.

![Auto Scaling](../../images/as-5.png)

### Set Forwarding Rules

- Configure forwarding rules to define how traffic should be distributed across your servers.
- Provide the port range for incoming traffic with **Public** and **Private** ports.

![Auto Scaling](../../images/as-6.png)

### Choose Image

- Select an operating system or application template to install on your server. You can also upload a custom ISO image for greater flexibility.

![Auto Scaling](../../images/as-16.png)

### Choose Plan

- Choose a plan based on your requirements like CPU, memory, storage, and bandwidth. You can also create a custom plan if needed.
- The cost will adjust according to the resources you select.

![Auto Scaling](../../images/as-7.png)

### Server Settings

- In server settings, you can add password to your server to enhance security. Click on **Set now**.
- Enter **Username** and **Password** then click on **Confirm** to add password.

![Auto Scaling](../../images/as-17.png)

### Capacity Planner

- Enter the minimum and maximum number of instances and enter the grace period in seconds.

![Auto Scaling](../../images/as-8.png)

### Set Up Policies

- A **Scale Up** policy is triggered when resource usage exceeds a defined threshold, adding more instances to handle increased demand.

![Auto Scaling](../../images/as-9.png)

- A **Scale Down** policy is triggered when resource demand drops, reducing the number of active instances to save costs.

![Auto Scaling](../../images/as-10.png)

- Click on **Expression** to add expression to your Scale up and Scale down policies. Provide the **Counter**, **Operator** and **Threshold** and click on **Submit**.

![Auto Scaling](../../images/as-15.png)

- Instead of reacting to real-time metrics, **Scheduled Policies** allow predefined scaling actions at specific times.

![Auto Scaling](../../images/as-11.png)

### Choose Auto-scaling Name

- Provide a unique **Auto-scaling Name** for your Auto-scaling to identify it easily in your dashboard.

![Auto Scaling](../../images/create-auto-scaling-inline-22660263.png)

### Create Auto-scaling

- Choose the desired **Billing Cycle** for your Auto-scaling. Autoscaling supports Monthly, Quarterly, Semiannually, Yearly, Bi-annually, and Tri-annually billing cycles.
- The billing rules include Date to Date, Fixed Calendar Month, Unfixed Calendar Month, Fixed Prorata, and Unfixed Prorata.
- Auto-scaling follows the same billing model as other scalable services to adapt to workload demands.
- Verify all the configuration details and review the price summary. Click on **Create** to create the Auto-scaling.

![Auto Scaling](../../images/as-14.png)

### Conclusion

Auto-scaling is a powerful feature that helps you maintain application performance, availability, and cost efficiency by automatically adjusting resources based on demand. By carefully configuring networks, load balancers, server settings, and scaling policies, you can ensure that your workloads adapt seamlessly to varying traffic patterns.
