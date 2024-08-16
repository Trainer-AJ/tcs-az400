# tcs-az400

```
echo "# tcs-az400" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Trainer-AJ/tcs-az400.git
git push -u origin main
```

# logs 
```
browserTimings 

requests 

// Count of failed and successful requests over time
requests
| extend success=tobool(success)
| where timestamp > datetime("2024-08-16T11:36:00.000Z") and timestamp < datetime("2024-08-16T12:36:00.000Z")
| where cloud_RoleName == 'mangulaptop97'
| where client_Type == "PC"
| summarize
    succeeded=sumif(itemCount, success == true),
    failed=sumif(itemCount, success == false)
    by bin(timestamp, 1m)
| render timechart

// Percentiles of request duration over time
requests
| where timestamp > datetime("2024-08-16T11:36:00.000Z") and timestamp < datetime("2024-08-16T12:36:00.000Z")
| where cloud_RoleName == 'mangulaptop97'
| where client_Type == "PC"
| summarize percentiles(duration, 50, 75, 95) by bin(timestamp, 1m)
| render timechart

// Count of failed and successful calls over time
dependencies
| extend success=tobool(success)
| where timestamp > datetime("2024-08-16T11:36:00.000Z") and timestamp < datetime("2024-08-16T12:36:00.000Z")
| where cloud_RoleName == 'mangulaptop97'
| where client_Type == "PC"
| summarize
    succeeded=sumif(itemCount, success == true),
    failed=sumif(itemCount, success == false)
    by target, bin(timestamp, 1m)
| render timechart

// 95th percentile of dependency duration by target over time
dependencies
| where timestamp > datetime("2024-08-16T11:36:00.000Z") and timestamp < datetime("2024-08-16T12:36:00.000Z")
| where cloud_RoleName == 'mangulaptop97'
| where client_Type == "PC"
| summarize percentiles(duration, 95) by bin(timestamp, 1m), target
| render timechart

// Operations performance 
// Calculate request count and duration by operations. 
// To create an alert for this query, click '+ New alert rule'
requests
| summarize RequestsCount=sum(itemCount), AverageDuration=avg(duration), percentiles(duration, 50, 95, 99) by operation_Name // you can replace 'operation_Name' with another value to segment by a different property
| order by RequestsCount desc // order from highest to lower (descending)
```

Use Cases - Logic App 
https://learn.microsoft.com/en-us/azure/logic-apps/logic-apps-examples-and-scenarios

Sure! Let's break down the difference between **polling triggers** and **push triggers** in a clear and simple way:

### Polling Trigger

- **How It Works:** 
  - **Checks Regularly:** The system periodically checks a service (like a website or API) to see if there's new data or an event that meets the trigger condition.
  - **Scheduled Intervals:** It checks based on a pre-set schedule, such as every 5 minutes or every hour.
  
- **When It Triggers:**
  - **Condition Met on Check:** If the trigger condition is met during one of these scheduled checks, the workflow starts and uses the data found at that time.
  
- **Example:** 
  - Imagine a system that checks an email inbox every 10 minutes. If a new email meeting certain criteria arrives, it triggers a workflow to handle that email.

### Push Trigger

- **How It Works:**
  - **Waits for Events:** The system sits and waits at a service endpoint (like a specific URL or server).
  - **Immediate Response:** When the service sends data or an event that meets the trigger condition, the system immediately triggers the workflow.

- **When It Triggers:**
  - **Condition Met on Arrival:** The workflow starts right away when the data or event arrives, without waiting for a scheduled check.

- **Example:**
  - Think of a system that waits for notifications from a messaging service. As soon as a new message meeting certain criteria arrives, the workflow is triggered instantly.

### Summary:

- **Polling Trigger:** Regularly checks at scheduled times to see if a condition is met.
- **Push Trigger:** Waits and reacts instantly when the condition is met or when data arrives.
