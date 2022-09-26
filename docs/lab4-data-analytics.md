# Lab 4 - Data Analytics

## Introduction

One of the first things your data analysts and data engineers will need
to do is analyse the raw data, with a view to preparing and transforming
it to a state that will be consumable by AI/ML model algorithms.

In this lab, we're going to use a powerful toolset combining

-   An in-memory data analytics engine called Trino. Trino provides high speed access to many different on-premises and cloud based data sources. These include relational and no-SQL databases, object stores over S3 interfaces, Streaming data from Kafka and many more. Trino abstracts the actual underlying data store implementation and provides a uniform ANSI SQL interface, to access its many supported data stores.

-   A visualization tool called Superset, which will use Trino as the backing data source.

The combination of these two tools will provide powerful data analytics
capabilities, critical at this stage in the workflow.

This diagram illustrates what we're implementing:

<img src="images/lab4-data-analytics/image19.png" alt="drawing" width="600">

You can see Trino is an SQL exposing abstraction in front of actual data
located in Kafka and S3 Object storage. No data is moved - rather Trino
provides a high speed parallel access mechanism for Kafka and S3
allowing Superset to easily display charts and dashboards.

To save time, the workshop administrators have already wired up the SQL
exposing engine Trino to two backing datasets:

1.  To a CSV file over an S3 interface. This CSV file is located in an underlying Object storage implementation called Minio. The file contains demographic type data on our customer data set, data such as gender, whether they have dependents and other demographic features.

2.  To Streaming data located in an Apache Kafka store on the OpenShift cluster. This dataset contains product consumption for the same customers as are in the CSV file. Each record is labelled indicating whether that customer churned or not.

In Superset, using Trino, we\'ve created two logical SQL tables
corresponding to underlying data sets as well as a query joining them on
customer id.

## Instructions for the Trino backed Superset workshop

Login to OpenShift using the credentials your administrator gave you.
Ensure your workshop project ml-workshop is selected.

The first thing you will do is login to Superset.  
1. Choose the **Administration perspective**.
2. Click to **Networking > Routes**.
3.  Filter on the word Superset and open that route, by clicking on the URL as shown.

<img src="images/lab4-data-analytics/image15.png" alt="drawing" width="600">

4.  If prompted, enter credentials ***admin / admin***.

<img src="images/lab4-data-analytics/image14.png" alt="drawing" width="600">

   **Note:** As this is a shared service between all participants, and the setup has already been done by your instructor. Here we will just describe you the steps we took to connect Superset to Trino and from there to underlying data.

5. Click **Data** in the toolbar drop-down list.
6. Click **Databases**  
   Superset displays a list of currently-configured databases.
7. Move the mouse over the **Trino** database and observe the **Edit** button (pen) appear.
8. Click the **Edit** button.  
   Superset displays the **Edit database** diaglog box.

<img src="images/lab4-data-analytics/image16.png" alt="drawing" width="600">

  Observe that we only needed to add the URI ***trino:/admin@trino-service:8080/*** to connect to Trino as shown. 

### Test the Connection.

1. Click the **Test Connection** button  
   Observe the ```Connection looks good``` message appear on the bottom right of the browser window.

<img src="images/lab4-data-analytics/image22.png" alt="drawing" width="600">

5. Click the **Advanced** tab in the **Edit database** diaglog box.  
   Superset displays a list of configuration groups to edit.
6. Click the **SQL Lab** button.  
   
<img src="images/lab4-data-analytics/image1.png" alt="drawing" width="300">  

   Observe the variety of SQL connection settings  
7. Click **CLOSE**.

6. CLick **SQL LAB > Saved Queries** in the main Superset toolbar. 
7. Edit the query ***Kafka-CSV-Join*** as shown  
   **Note:** Your query may be named differently

<img src="images/lab4-data-analytics/image12.png" alt="drawing" width="600">

Earlier the workshop, the workshop facilitatore created two _virtual tables_ to hold the data. (A virtual table is a table that for all intents and purposes acts like a database, but is not). The virtual tables' details are:
* Virtual table 1: (hive.default.customer1) that uses the CSV data in our Minio S3 Object store as it's actual data - located in the bucket ***Rawdata***.  
* Virtual table2:  Backed by Kafka streaming data. (In this example it is the customer product-consumption data.)

What you will see in this lab is how Trino presents a standard SQL interface for non-SQL data stores (CSV and Kafka).

Now Trino allows us to create a SQL Join across data that resides in S3 Object storage and Kafka as follows:
```sql
SELECT  kafkaData.*, s3Data.*
FROM    customerchurn.default.data kafkaData,
        hive.default.customer1 s3Data
WHERE   cast(kafkaData.customerId as VARCHAR) = s3Data.customerId
```

8.  **Run** the Query. Notice the result set spanning data covering S3 and Kafka, joined on *customerId.*    
  ```Observe how cool that is! :-)```

9. Click **Explore**.
   Superset prompts you to sve the result set.  

  <img src="images/lab4-data-analytics/image6.png" alt="drawing" width="600">


10. Click the **Save as new** radio button
11. Type ```Kafka-CSV-Join-``` and append your user name in the text box. E.g. ```Kafka-CSV-Join-user29```
12. Click **SAVE & EXPLORE**

<img src="images/lab4-data-analytics/image21.png" alt="drawing" width="600">  

 > **Note:**  You may see an error saving the dataset. Ignore it.

13.  Click to **Data > DataSets** in the main toolbar.
14. Locate your new dataset and click it to open it.

<img src="images/lab4-data-analytics/image11.png" alt="drawing" width="600">

12. By default ***Table*** Visualisation Type is selected

<img src="images/lab4-data-analytics/image18.png" alt="drawing" width="600">

13. Click the **Table** icon in the ```VISUALIZATION``` section.  
14. Click **All charts** at the top of the ```chart explorer``` panel.
   Observe the large number of Visualization Types to choose from. 
14. Click **Bar Chart**

<img src="images/lab4-data-analytics/image24.png" alt="drawing" width="600">  

15. Click **SELECT**

You can now start visualising and understanding your data. First we'll create a bar chart representation of the entire dataset, representing the count of the different categories of *Primary Channel*:

- *Branch*
- *Mobile and*
- *No* primary channel.

For this report we will remove any default filters.  
16. Locate the **TIME RANGE** category in the explorer panel. If it is not set to **No filter**, click the option and set the value of**RANGE TYPE** to **No filter**.  Click **Apply**.

<img src="images/lab4-data-analytics/image25.png" alt="drawing" width="600">

Select ***Count*** under ***Metrics*** and select *PrimaryChannel* under ***Series***.

Name the chart ***Count-PrimaryChannel-userXX*** (in my case***Count-PrimaryChannel-user29***) and click **Save**.

<img src="images/lab4-data-analytics/image3.png" alt="drawing" width="600">

This will cause the query to run - and you will be presented with this bar chart - showing the breakdown of the resultset by Primary Channel, Branch, Mobile or None.

<img src="images/lab4-data-analytics/image10.png" alt="drawing" width="600">

17. Now we'll create a Pie Chart - and add another dimension - *account type*.

On your open Bar Chart screen, click **Bar Chart**. On the popup click **Pie Chart**.

<img src="images/lab4-data-analytics/image7.png" alt="drawing" width="600">

Now make the following changes:

-   On the **Group By** dropdown, add ***accounttype*** to already present **primarychannel**

-   Name the chart ***Count-ChannelByAccountType-userXX*** (in my case ***Count-ChannelByAccountType-user29***) and click **Save**.  
- Set the **METRIC** to ```f(x) count```  
-   Go with the defaults on the popup. Click **Save As** then **Save**

<img src="images/lab4-data-analytics/image23.png" alt="drawing" width="600">

This will cause the following pie chart to display - grouping *Primary Channel* by *Account Type*

<img src="images/lab4-data-analytics/image2.png" alt="drawing" width="600">

18. Next, we're going to showcase another unusual though informative visualization - the Sunburst Chart. It allows you to visualise splits of your data with varying degrees of granularity - within the same chart. On your open Pie Chart screen, click **Pie Chart** then on the popup, scroll down and click **Sunburst Chart** as shown:

<img src="images/lab4-data-analytics/image29.png" alt="drawing" width="600">

Make the following changes

-   Name the chart ***CreditRating-Distribution-userXX*** (in my case ***CreditRating-Distribution-user29***)

-   On the **Hierarchy** dropdown, select
    -   **creditrating**
    -   **accounttype**
    -   **hascreditcard**
        -   **debitcard**
-   click **Save**

<img src="images/lab4-data-analytics/image27.png" alt="drawing" width="600">

Confirm by clicking **Save As** then **Save**

<img src="images/lab4-data-analytics/image26.png" alt="drawing" width="600">

A chart similar to the following will appear.

<img src="images/lab4-data-analytics/image5.png" alt="drawing" width="600">

If you hover over the inner circle, the breakdown according to the first hierarchical element is shown, in my case *medium* credit rating.

You can see, you can also further refine, by hovering out towards over the outer circle - giving a very fine grained breakdown - according to the 4 hierarchies:

<img src="images/lab4-data-analytics/image20.png" alt="drawing" width="600">

Any of these datasets can be easily exported to JSON or CSV - as shown below. Then fed for example to an AI model training use case.

<img src="images/lab4-data-analytics/image28.png" alt="drawing" width="600">

15. Finally we're going to show you how to create a dashboard - to which we can add previously saved charts. Choose Dashboards -\> Add Dashboard as shown:

<img src="images/lab4-data-analytics/image9.png" alt="drawing" width="600">

Name it and choose the Charts tab:

<img src="images/lab4-data-analytics/image8.png" alt="drawing" width="600">

You can simply drag your charts from the right over to the display panel
on the left as shown. You can also make them dynamic by choosing a
refresh interval. Very cool!

<img src="images/lab4-data-analytics/image4.png" alt="drawing" width="600">

Feel free to continue to experiment with different ways of accessing and
visualising the underlying data.
