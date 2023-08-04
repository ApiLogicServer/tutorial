# Behave Creates Executable Test Suite, Documentation

You can optionally use the Behave test framework to:

1. **Create and Run an Executable Test Suite:** in your IDE, create test definitions (similar to what is shown in the report below), and Python code to execute tests.  You can then execute your test suite with 1 command.

2. **Requirements and Test Documentation:** as shown below, you can then create a wiki report that documents your requirements, and the tests (**Scenarios**) that confirm their proper operation.

   * **Logic Documentation:** the report integrates your logic, including a logic report showing your logic (rules and Python), and a Logic Log that shows exactly how the rules executed.  Logic Doc can further contribute to Agile Collaboration.

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/behave-summary.png?raw=true"  height="600"></figure>

[Behave](https://behave.readthedocs.io/en/stable/tutorial.html) is a framework for defining and executing tests.  It is based on [TDD (Test Driven Development)](http://dannorth.net/introducing-bdd/), an Agile approach for defining system requirements as executable tests.

&nbsp;&nbsp;

# Using Behave

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/TDD-ide.png?raw=true"></figure>

Behave is pre-installed with API Logic Server.  Use it as shown above:

1. Create `.feature` files to define ***Scenarios*** (aka tests) for ***Features*** (aka Stories)

2. Code `.py` files to implement Scenario tests

3. Run Test Suite: Launch Configuration `Behave Run`.  This runs all your Scenarios, and produces a summary report of your Features and the test results.

4. Report: Launch Configuration `Behave Report` to create the wiki file shown at the top of this page.

These steps are further defined, below.  Explore the samples in the sample project.

&nbsp;&nbsp;

## 1. Create `.feature` file to define Scenario

Feature (aka Story) files are designed to promote IT / business user collaboration.  

&nbsp;&nbsp;

## 2. Code `.py` file to implement test

Implement your tests in Python.  Here, the tests are largely _read existing data_, _run transaction_, and _test results_, using the API.  You can obtain the URLs from the swagger.

Key points:

* Link your scenario / implementations with annotations, as shown for _Order Placed with excessive quantity_.

* Include the `test_utils.prt()` call; be sure to use specify the scenario name as the 2nd argument.  This is what drives the name of the Logic Log file, discussed below.

* Optionally, include a Python docstring on your `when` implementation as shown above, delimited by `"""` strings (see _"Familiar logic pattern"_ in the screen shot, above). If provided, this will be written into the wiki report.

* Important: the system assumes the following line identifies the scenario_name; be sure to include it.

&nbsp;&nbsp;

## 3. Run Test Suite: Launch Configuration `Behave Run`

You can now execute your Test Suite.  Run the `Behave Run` Launch Configuration, and Behave will run all of the tests, producing the outputs (`behave.log` and `<scenario.logs>` shown above.

* Windows users will need to run `Windows Behave Run`

* You can run just 1 scenario using `Behave Scenario`

* You can set breakpoints in your tests

The server must be running for these tests.  Use the Launch Configuration `ApiLogicServer`, or `python api_logic_server_run.py`.  The latter does not run the debugger, which you may find more convenient since changes to your test code won't restart the server.

&nbsp;&nbsp;

## 4. Report: Launch Configuration `Behave Report'

Run this to create the wiki reports from the logs in step 3.


&nbsp;
&nbsp;


# Behave Logic Report
&nbsp;
&nbsp;
## Feature: About Sample  
  
&nbsp;
&nbsp;
### Scenario: Transaction Processing
&emsp;  Scenario: Transaction Processing  
&emsp;&emsp;    Given Sample Database  
&emsp;&emsp;    When Transactions are submitted  
&emsp;&emsp;    Then Enforce business policies with Logic (rules + code)  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Rules Used** in Scenario: Transaction Processing
```
  Category  
    1. Constraint Function: <function declare_logic.<locals>.valid_category_description at 0x108dac7c0>   
  
```
**Logic Log** in Scenario: Transaction Processing
```

The following rules have been activate
 - 2023-07-16 19:02:20,590 - logic_logger - DEBU
Rule Bank[0x1087c4490] (loaded 2023-07-16 19:02:15.106566
Mapped Class[Customer] rules
  Constraint Function: None
  Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>
  RowEvent Customer.customer_defaults()
  Constraint Function: None
  Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>
  Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None
Mapped Class[Order] rules
  Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None
  RowEvent Order.congratulate_sales_rep()
  RowEvent Order.order_defaults()
  Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None
  RowEvent Order.clone_order()
Mapped Class[OrderDetail] rules
  Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...
  Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice
  RowEvent OrderDetail.order_detail_defaults()
  Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDat
Mapped Class[Employee] rules
  Constraint Function: None
  Constraint Function: <function declare_logic.<locals>.raise_over_20_percent at 0x108dacd60>
  Copy to: EmployeeAudi
Mapped Class[Category] rules
  Constraint Function: <function declare_logic.<locals>.valid_category_description at 0x108dac7c0>
Mapped Class[Product] rules
  Derive Product.UnitsInStock as Formula (1): <function
  Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108dac9a0>
Logic Bank - 28 rules loaded - 2023-07-16 19:02:20,594 - logic_logger - INF

Logic Phase:		BEFORE COMMIT(session=0x109325a10)          						 - 2023-07-16 19:02:20,641 - logic_logger - DEBU

Logic Phase:		BEFORE COMMIT(session=0x10933bb10)          						 - 2023-07-16 19:02:20,714 - logic_logger - DEBU

Logic Phase:		BEFORE COMMIT(session=0x10939d490)          						 - 2023-07-16 19:02:20,761 - logic_logger - DEBU

Logic Phase:		BEFORE COMMIT(session=0x1093a2490)          						 - 2023-07-16 19:02:20,792 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x1093a2490) (sqlalchemy before_flush)			 - 2023-07-16 19:02:20,793 - logic_logger - INF
..CategoryTableNameTest[not available] {Update - client} Id: 1, CategoryName: Beverages, Description:  [Soft drinks, coffees, teas, beers, and ales-->] x, Client_id: 1  row: 0x1093a2e10  session: 0x1093a2490  ins_upd_dlt: upd - 2023-07-16 19:02:20,793 - logic_logger - INF
..CategoryTableNameTest[not available] {Constraint Failure: x cannot be 'x'} Id: 1, CategoryName: Beverages, Description:  [Soft drinks, coffees, teas, beers, and ales-->] x, Client_id: 1  row: 0x1093a2e10  session: 0x1093a2490  ins_upd_dlt: upd - 2023-07-16 19:02:20,794 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
## Feature: Application Integration  
  
&nbsp;
&nbsp;
### Scenario: GET Customer
&emsp;  Scenario: GET Customer  
&emsp;&emsp;    Given Customer Account: VINET  
&emsp;&emsp;    When GET Orders API  
&emsp;&emsp;    Then VINET retrieved  
  
&nbsp;
&nbsp;
### Scenario: GET Department
&emsp;  Scenario: GET Department  
&emsp;&emsp;    Given Department 2  
&emsp;&emsp;    When GET Department with SubDepartments API  
&emsp;&emsp;    Then SubDepartments returned  
  
&nbsp;
&nbsp;
## Feature: Optimistic Locking  
  
&nbsp;
&nbsp;
### Scenario: Get Category
&emsp;  Scenario: Get Category  
&emsp;&emsp;    Given Category: 1  
&emsp;&emsp;    When Get Cat1  
&emsp;&emsp;    Then Expected Cat1 Checksum  
  
&nbsp;
&nbsp;
### Scenario: Valid Checksum
&emsp;  Scenario: Valid Checksum  
&emsp;&emsp;    Given Category: 1  
&emsp;&emsp;    When Patch Valid Checksum  
&emsp;&emsp;    Then Valid Checksum, Invalid Description  
  
&nbsp;
&nbsp;
### Scenario: Missing Checksum
&emsp;  Scenario: Missing Checksum  
&emsp;&emsp;    Given Category: 1  
&emsp;&emsp;    When Patch Missing Checksum  
&emsp;&emsp;    Then Valid Checksum, Invalid Description  
  
&nbsp;
&nbsp;
### Scenario: Invalid Checksum
&emsp;  Scenario: Invalid Checksum  
&emsp;&emsp;    Given Category: 1  
&emsp;&emsp;    When Patch Invalid Checksum  
&emsp;&emsp;    Then Invalid Checksum  
  
&nbsp;
&nbsp;
## Feature: Place Order  
  
&nbsp;
&nbsp;
### Scenario: Good Order Custom Service
&emsp;  Scenario: Good Order Custom Service  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Good Order Placed  
&emsp;&emsp;    Then Logic adjusts Balance (demo: chain up)  
&emsp;&emsp;    Then Logic adjusts Products Reordered  
&emsp;&emsp;    Then Logic sends email to salesrep  
&emsp;&emsp;    Then Logic adjusts aggregates down on delete order  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Good Order Custom Service
   
We place an Order with an Order Detail.  It's one transaction.

Note how the `Order.OrderTotal` and `Customer.Balance` are *adjusted* as Order Details are processed.
Similarly, the `Product.UnitsShipped` is adjusted, and used to recompute `UnitsInStock`

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/declare-logic.png?raw=true"></figure>

> **Key Takeaway:** sum/count aggregates (e.g., `Customer.Balance`) automate ***chain up*** multi-table transactions.

**Events - Extensible Logic**

Inspect the log for __Hi, Andrew - Congratulate Nancy on their new order__. 

The `congratulate_sales_rep` event illustrates logic 
[Extensibility](https://apilogicserver.github.io/Docs/Logic/#extensibility-python-events) 
- using Python to provide logic not covered by rules, 
like non-database operations such as sending email or messages.

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/send-email.png?raw=true"></figure>

There are actually multiple kinds of events:

* *Before* row logic
* *After* row logic
* On *commit,* after all row logic has completed (as here), so that your code "sees" the full logic results

Events are passed the `row` and `old_row`, as well as `logic_row` which enables you to test the actual operation, chaining nest level, etc.

You can set breakpoints in events, and inspect these.



&nbsp;
&nbsp;


**Rules Used** in Scenario: Good Order Custom Service
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    4. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    5. RowEvent Order.order_defaults()   
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    7. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    8. RowEvent Order.congratulate_sales_rep()   
    9. RowEvent Order.clone_order()   
  OrderDetail  
    10. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    11. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
    12. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
    13. RowEvent OrderDetail.order_detail_defaults()   
  Product  
    14. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108dac9a0>)  
    15. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Good Order Custom Service
```

Logic Phase:		BEFORE COMMIT(session=0x1094036d0)          						 - 2023-07-16 19:02:20,958 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x1094036d0) (sqlalchemy before_flush)			 - 2023-07-16 19:02:20,958 - logic_logger - INF
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,959 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance: 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11, Client_id: 1  row: 0x109401cd0  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,965 - logic_logger - INF
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 1, UnitPrice: None, Quantity: 1, Discount: 0, Amount: None, ShippedDate: None  row: 0x1094037d0  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,966 - logic_logger - INF
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0, Amount: None, ShippedDate: None  row: 0x1094037d0  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,968 - logic_logger - INF
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1, Discount: 0, Amount: 18.0000000000, ShippedDate: None  row: 0x1094037d0  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,969 - logic_logger - INF
....Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal:  [None-->] 18.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,969 - logic_logger - INF
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 2120.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11, Client_id: 1  row: 0x109401cd0  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,970 - logic_logger - INF
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 39, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] 1  row: 0x1093f7e50  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,972 - logic_logger - INF
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [39-->] 38, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] 1  row: 0x1093f7e50  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,972 - logic_logger - INF
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 2, UnitPrice: None, Quantity: 2, Discount: 0, Amount: None, ShippedDate: None  row: 0x1093cb110  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,973 - logic_logger - INF
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0, Amount: None, ShippedDate: None  row: 0x1093cb110  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,974 - logic_logger - INF
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0, Amount: 38.0000000000, ShippedDate: None  row: 0x1093cb110  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,974 - logic_logger - INF
....Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal:  [18.0000000000-->] 56.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [1-->] 2, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,975 - logic_logger - INF
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2120.0000000000-->] 2158.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11, Client_id: 1  row: 0x109401cd0  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,976 - logic_logger - INF
....Product[2] {Update - Adjusting Product: UnitsShipped} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock: 17, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [0-->] 2  row: 0x1094229d0  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,978 - logic_logger - INF
....Product[2] {Formula UnitsInStock} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock:  [17-->] 15, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [0-->] 2  row: 0x1094229d0  session: 0x1094036d0  ins_upd_dlt: upd - 2023-07-16 19:02:20,978 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1094036d0)   										 - 2023-07-16 19:02:20,979 - logic_logger - INF
..Order[None] {Commit Event} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: 56.0000000000, Country: None, City: None, Ready: None, OrderDetailCount: 2, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,979 - logic_logger - INF
..Order[None] {Hi, Andrew - Congratulate Nancy on their new order} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: 56.0000000000, Country: None, City: None, Ready: None, OrderDetailCount: 2, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,981 - logic_logger - INF
..Order[None] {Illustrate database access (not subject to authorization)} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: 56.0000000000, Country: None, City: None, Ready: None, OrderDetailCount: 2, CloneFromOrder: None  row: 0x109403710  session: 0x1094036d0  ins_upd_dlt: ins - 2023-07-16 19:02:20,982 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Bad Order Custom Service
&emsp;  Scenario: Bad Order Custom Service  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order Placed with excessive quantity  
&emsp;&emsp;    Then Rejected per Check Credit  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Bad Order Custom Service
   
Familiar logic patterns:
* Constrain a derived result
* Chain up, to adjust parent sum/count aggregates

Logic Design ("Cocktail Napkin Design")
* Customer.Balance <= CreditLimit
* Customer.Balance = Sum(Order.AmountTotal where unshipped)
* Order.AmountTotal = Sum(OrderDetail.Amount)
* OrderDetail.Amount = Quantity * UnitPrice
* OrderDetail.UnitPrice = copy from Product



&nbsp;
&nbsp;


**Rules Used** in Scenario: Bad Order Custom Service
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Constraint Function: None   
    4. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    5. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    6. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    7. RowEvent Order.order_defaults()   
    8. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    9. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    10. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
    11. RowEvent OrderDetail.order_detail_defaults()   
    12. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
  Product  
    13. Derive Product.UnitsShipped as Sum(OrderDetail.Quantity Where <function declare_logic.<locals>.<lambda> at 0x108dac9a0>)  
    14. Derive Product.UnitsInStock as Formula (1): <function>  
  
```
**Logic Log** in Scenario: Bad Order Custom Service
```

Logic Phase:		BEFORE COMMIT(session=0x10948bbd0)          						 - 2023-07-16 19:02:21,324 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x10948bbd0) (sqlalchemy before_flush)			 - 2023-07-16 19:02:21,324 - logic_logger - INF
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 1, UnitPrice: None, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10948bcd0  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,325 - logic_logger - INF
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: None, ShippedDate: None  row: 0x10948bcd0  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,326 - logic_logger - INF
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 1, UnitPrice: 18.0000000000, Quantity: 1111, Discount: 0, Amount: 19998.0000000000, ShippedDate: None  row: 0x10948bcd0  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,326 - logic_logger - INF
....Order[None] {Adjustment logic chaining deferred for this parent parent do_defer_adjustment: True, is_parent_submitted: True, is_parent_row_processed: False, Order} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal:  [None-->] 19998.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1, CloneFromOrder: None  row: 0x10948ba50  session: 0x10948bbd0  ins_upd_dlt: * - 2023-07-16 19:02:21,327 - logic_logger - INF
....Product[1] {Update - Adjusting Product: UnitsShipped} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock: 39, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] 1111  row: 0x10948ae50  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,327 - logic_logger - INF
....Product[1] {Formula UnitsInStock} Id: 1, ProductName: Chai, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 10 boxes x 20 bags, UnitPrice: 18.0000000000, UnitsInStock:  [39-->] -1072, UnitsOnOrder: 0, ReorderLevel: 10, Discontinued: 0, UnitsShipped:  [0-->] 1111  row: 0x10948ae50  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,328 - logic_logger - INF
..OrderDetail[None] {Insert - client} Id: None, OrderId: None, ProductId: 2, UnitPrice: None, Quantity: 2, Discount: 0, Amount: None, ShippedDate: None  row: 0x10948b290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,329 - logic_logger - INF
..OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0, Amount: None, ShippedDate: None  row: 0x10948b290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,330 - logic_logger - INF
..OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId: 2, UnitPrice: 19.0000000000, Quantity: 2, Discount: 0, Amount: 38.0000000000, ShippedDate: None  row: 0x10948b290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,331 - logic_logger - INF
....Order[None] {Adjustment logic chaining deferred for this parent parent do_defer_adjustment: True, is_parent_submitted: True, is_parent_row_processed: False, Order} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal:  [19998.0000000000-->] 20036.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [1-->] 2, CloneFromOrder: None  row: 0x10948ba50  session: 0x10948bbd0  ins_upd_dlt: * - 2023-07-16 19:02:21,331 - logic_logger - INF
....Product[2] {Update - Adjusting Product: UnitsShipped} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock: 17, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [0-->] 2  row: 0x1094766d0  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,332 - logic_logger - INF
....Product[2] {Formula UnitsInStock} Id: 2, ProductName: Chang, SupplierId: 1, CategoryId: 1, QuantityPerUnit: 24 - 12 oz bottles, UnitPrice: 19.0000000000, UnitsInStock:  [17-->] 15, UnitsOnOrder: 40, ReorderLevel: 25, Discontinued: 0, UnitsShipped:  [0-->] 2  row: 0x1094766d0  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,332 - logic_logger - INF
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 10, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: 20036.0000000000, Country: None, City: None, Ready: None, OrderDetailCount: 2, CloneFromOrder: None  row: 0x10948ba50  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:21,333 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22138.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11, Client_id: 1  row: 0x109475cd0  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,335 - logic_logger - INF
....Customer[ALFKI] {Constraint Failure: balance (22138.00) exceeds credit (2300.00)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 22138.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11, Client_id: 1  row: 0x109475cd0  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:21,336 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Alter Item Qty to exceed credit
&emsp;  Scenario: Alter Item Qty to exceed credit  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order Detail Quantity altered very high  
&emsp;&emsp;    Then Rejected per Check Credit  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Alter Item Qty to exceed credit
   
Same constraint as above.

> **Key Takeaway:** Automatic Reuse (_design one, solve many_)


&nbsp;
&nbsp;


**Rules Used** in Scenario: Alter Item Qty to exceed credit
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Constraint Function: None   
    4. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    5. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    6. RowEvent Order.order_defaults()   
    7. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    8. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
  OrderDetail  
    9. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    10. RowEvent OrderDetail.order_detail_defaults()   
  
```
**Logic Log** in Scenario: Alter Item Qty to exceed credit
```

Logic Phase:		BEFORE COMMIT(session=0x109486090)          						 - 2023-07-16 19:02:21,434 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x109486090) (sqlalchemy before_flush)			 - 2023-07-16 19:02:21,434 - logic_logger - INF
..OrderDetail[1040] {Update - client} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount: 684.0000000000, ShippedDate: None  row: 0x109486d10  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,435 - logic_logger - INF
..OrderDetail[1040] {Formula Amount} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x109486d10  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,435 - logic_logger - INF
..OrderDetail[1040] {Prune Formula: ShippedDate [['Order.ShippedDate']]} Id: 1040, OrderId: 10643, ProductId: 28, UnitPrice: 45.6000000000, Quantity:  [15-->] 1110, Discount: 0.25, Amount:  [684.0000000000-->] 50616.0000000000, ShippedDate: None  row: 0x109486d10  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,435 - logic_logger - INF
....Order[10643] {Update - Adjusting Order: AmountTotal} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-09-22, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal:  [1086.00-->] 51018.0000000000, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x10947d210  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,437 - logic_logger - INF
......Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10, Client_id: 1  row: 0x1093a7110  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,439 - logic_logger - INF
......Customer[ALFKI] {Constraint Failure: balance (52034.00) exceeds credit (2300.00)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 52034.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount: 10, Client_id: 1  row: 0x1093a7110  session: 0x109486090  ins_upd_dlt: upd - 2023-07-16 19:02:21,439 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Alter Required Date - adjust logic pruned
&emsp;  Scenario: Alter Required Date - adjust logic pruned  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order RequiredDate altered (2013-10-13)  
&emsp;&emsp;    Then Balance not adjusted  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Alter Required Date - adjust logic pruned
   
We set `Order.RequiredDate`.

This is a normal update.  Nothing depends on the columns altered, so this has no effect on the related Customer, Order Details or Products.  Contrast this to the *Cascade Update Test* and the *Custom Service* test, where logic chaining affects related rows.  Only the commit event fires.

> **Key Takeaway:** rule pruning automatically avoids unnecessary SQL overhead.



&nbsp;
&nbsp;


**Rules Used** in Scenario: Alter Required Date - adjust logic pruned
```
  Customer  
    1. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    2. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    3. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    4. RowEvent Order.order_defaults()   
    5. RowEvent Order.congratulate_sales_rep()   
    6. RowEvent Order.clone_order()   
  
```
**Logic Log** in Scenario: Alter Required Date - adjust logic pruned
```

Logic Phase:		BEFORE COMMIT(session=0x10948f110)          						 - 2023-07-16 19:02:21,531 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x10948f110) (sqlalchemy before_flush)			 - 2023-07-16 19:02:21,532 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-09-22-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x10947e990  session: 0x10948f110  ins_upd_dlt: upd - 2023-07-16 19:02:21,532 - logic_logger - INF
Logic Phase:		COMMIT(session=0x10948f110)   										 - 2023-07-16 19:02:21,533 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate:  [2013-09-22-->] 2013-10-13 00:00:00, ShippedDate: None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x10947e990  session: 0x10948f110  ins_upd_dlt: upd - 2023-07-16 19:02:21,534 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Set Shipped - adjust logic reuse
&emsp;  Scenario: Set Shipped - adjust logic reuse  
&emsp;&emsp;    Given Customer Account: ALFKI  
&emsp;&emsp;    When Order ShippedDate altered (2013-10-13)  
&emsp;&emsp;    Then Balance reduced 1086  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Set Shipped - adjust logic reuse
   
We set `Order.ShippedDate`.

This cascades to the Order Details, per the `derive=models.OrderDetail.ShippedDate` rule.

This chains to adjust the `Product.UnitsShipped` and recomputes `UnitsInStock`, as above

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/order-shipped-date.png?raw=true"></figure>


> **Key Takeaway:** parent references (e.g., `OrderDetail.ShippedDate`) automate ***chain-down*** multi-table transactions.

> **Key Takeaway:** Automatic Reuse (_design one, solve many_)



&nbsp;
&nbsp;


**Rules Used** in Scenario: Set Shipped - adjust logic reuse
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    4. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    5. RowEvent Order.order_defaults()   
    6. RowEvent Order.congratulate_sales_rep()   
    7. RowEvent Order.clone_order()   
  
```
**Logic Log** in Scenario: Set Shipped - adjust logic reuse
```

Logic Phase:		BEFORE COMMIT(session=0x10948c650)          						 - 2023-07-16 19:02:21,706 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x10948c650) (sqlalchemy before_flush)			 - 2023-07-16 19:02:21,707 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x109434910  session: 0x10948c650  ins_upd_dlt: upd - 2023-07-16 19:02:21,707 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 1016.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [10-->] 9, Client_id: 1  row: 0x109456410  session: 0x10948c650  ins_upd_dlt: upd - 2023-07-16 19:02:21,708 - logic_logger - INF
Logic Phase:		COMMIT(session=0x10948c650)   										 - 2023-07-16 19:02:21,710 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [None-->] 2013-10-13, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x109434910  session: 0x10948c650  ins_upd_dlt: upd - 2023-07-16 19:02:21,711 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Reset Shipped - adjust logic reuse
&emsp;  Scenario: Reset Shipped - adjust logic reuse  
&emsp;&emsp;    Given Shipped Order  
&emsp;&emsp;    When Order ShippedDate set to None  
&emsp;&emsp;    Then Logic adjusts Balance by -1086  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Reset Shipped - adjust logic reuse
   
Same logic as above.

> **Key Takeaway:** Automatic Reuse (_design one, solve many_)


&nbsp;
&nbsp;


**Rules Used** in Scenario: Reset Shipped - adjust logic reuse
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    4. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    5. RowEvent Order.order_defaults()   
    6. RowEvent Order.congratulate_sales_rep()   
    7. RowEvent Order.clone_order()   
  
```
**Logic Log** in Scenario: Reset Shipped - adjust logic reuse
```

Logic Phase:		BEFORE COMMIT(session=0x1096a1690)          						 - 2023-07-16 19:02:21,898 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x1096a1690) (sqlalchemy before_flush)			 - 2023-07-16 19:02:21,898 - logic_logger - INF
..Order[10643] {Update - client} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x1096a2c50  session: 0x1096a1690  ins_upd_dlt: upd - 2023-07-16 19:02:21,898 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: Balance, UnpaidOrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [1016.0000000000-->] 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount: 15, UnpaidOrderCount:  [9-->] 10, Client_id: 1  row: 0x10948b410  session: 0x1096a1690  ins_upd_dlt: upd - 2023-07-16 19:02:21,900 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1096a1690)   										 - 2023-07-16 19:02:21,902 - logic_logger - INF
..Order[10643] {Commit Event} Id: 10643, CustomerId: ALFKI, EmployeeId: 6, OrderDate: 2013-08-25, RequiredDate: 2013-10-13, ShippedDate:  [2013-10-13-->] None, ShipVia: 1, Freight: 29.4600000000, ShipName: Alfreds Futterkiste, ShipAddress: Obere Str. 57, ShipCity: Berlin, ShipRegion: Western Europe, ShipZip: 12209, ShipCountry: Germany, AmountTotal: 1086.00, Country: None, City: None, Ready: True, OrderDetailCount: 3, CloneFromOrder: None  row: 0x1096a2c50  session: 0x1096a1690  ins_upd_dlt: upd - 2023-07-16 19:02:21,902 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Clone Existing Order
&emsp;  Scenario: Clone Existing Order  
&emsp;&emsp;    Given Shipped Order  
&emsp;&emsp;    When Cloning Existing Order  
&emsp;&emsp;    Then Logic Copies ClonedFrom OrderDetails  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Clone Existing Order
   
We create an order, setting CloneFromOrder.

This copies the CloneFromOrder OrderDetails to our new Order.

The copy operation is automated using `logic_row.copy_children()`:

1. `place_order.feature` defines the test

2. `place_order.py` implements the test.  It uses the API to Post an Order, setting `CloneFromOrder` to trigger the copy logic

3. `declare_logic.py` implements the logic, by invoking `logic_row.copy_children()`.  `which` defines which children to copy, here just `OrderDetailList`

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/clone-order.png?raw=true"></figure>

`CopyChildren` For more information, [see here](https://github.com/valhuber/LogicBank/wiki/Copy-Children)

    Useful in row event handlers to copy multiple children types to self from copy_from children.

    child-spec := < ‘child-list-name’ | < ‘child-list-name = parent-list-name’ >
    child-list-spec := [child-spec | (child-spec, child-list-spec)]

    Eg. RowEvent on Order
        which = ["OrderDetailList"]
        logic_row.copy_children(copy_from=row.parent, which_children=which)

    Eg, test/copy_children:
        child_list_spec = [
            ("MileStoneList",
                ["DeliverableList"]  # for each Milestone, get the Deliverables
            ),
            "StaffList"
        ]

> **Key Takeaway:** copy_children provides a deep-copy service.



&nbsp;
&nbsp;


**Rules Used** in Scenario: Clone Existing Order
```
  Customer  
    1. RowEvent Customer.customer_defaults()   
    2. Derive Customer.UnpaidOrderCount as Count(<class 'database.models.Order'> Where <function declare_logic.<locals>.<lambda> at 0x108dacae0>)  
    3. Constraint Function: None   
    4. Derive Customer.Balance as Sum(Order.AmountTotal Where <function declare_logic.<locals>.<lambda> at 0x10890ad40>)  
    5. Derive Customer.OrderCount as Count(<class 'database.models.Order'> Where None)  
  Order  
    6. RowEvent Order.order_defaults()   
    7. Derive Order.OrderDetailCount as Count(<class 'database.models.OrderDetail'> Where None)  
    8. Derive Order.AmountTotal as Sum(OrderDetail.Amount Where None)  
    9. RowEvent Order.clone_order()   
  OrderDetail  
    10. Derive OrderDetail.Amount as Formula (1): as_expression=lambda row: row.UnitPrice * row.Qua [...]  
    11. Derive OrderDetail.ShippedDate as Formula (2): row.Order.ShippedDate  
    12. Derive OrderDetail.UnitPrice as Copy(Product.UnitPrice)  
    13. RowEvent OrderDetail.order_detail_defaults()   
  
```
**Logic Log** in Scenario: Clone Existing Order
```

Logic Phase:		BEFORE COMMIT(session=0x10948bbd0)          						 - 2023-07-16 19:02:22,073 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x10948bbd0) (sqlalchemy before_flush)			 - 2023-07-16 19:02:22,074 - logic_logger - INF
..Order[None] {Insert - client} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None, CloneFromOrder: 10643  row: 0x109489290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:22,074 - logic_logger - INF
....Customer[ALFKI] {Update - Adjusting Customer: UnpaidOrderCount, OrderCount} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance: 2102.0000000000, CreditLimit: 2300.0000000000, OrderCount:  [15-->] 16, UnpaidOrderCount:  [10-->] 11, Client_id: 1  row: 0x1096b8f90  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:22,079 - logic_logger - INF
..Order[None] {Begin copy_children} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal: None, Country: None, City: None, Ready: None, OrderDetailCount: None, CloneFromOrder: 10643  row: 0x109489290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:22,080 - logic_logger - INF
....OrderDetail[None] {Insert - Copy Children OrderDetailList} Id: None, OrderId: None, ProductId:  [None-->] 28, UnitPrice: None, Quantity:  [None-->] 15, Discount:  [None-->] 0.25, Amount: None, ShippedDate: None  row: 0x109394290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:22,081 - logic_logger - INF
....OrderDetail[None] {copy_rules for role: Product - UnitPrice} Id: None, OrderId: None, ProductId:  [None-->] 28, UnitPrice:  [None-->] 45.6000000000, Quantity:  [None-->] 15, Discount:  [None-->] 0.25, Amount: None, ShippedDate: None  row: 0x109394290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:22,082 - logic_logger - INF
....OrderDetail[None] {Formula Amount} Id: None, OrderId: None, ProductId:  [None-->] 28, UnitPrice:  [None-->] 45.6000000000, Quantity:  [None-->] 15, Discount:  [None-->] 0.25, Amount:  [None-->] 684.0000000000, ShippedDate: None  row: 0x109394290  session: 0x10948bbd0  ins_upd_dlt: ins - 2023-07-16 19:02:22,083 - logic_logger - INF
......Order[None] {Update - Adjusting Order: AmountTotal, OrderDetailCount} Id: None, CustomerId: ALFKI, EmployeeId: 1, OrderDate: None, RequiredDate: None, ShippedDate: None, ShipVia: None, Freight: 11, ShipName: None, ShipAddress: None, ShipCity: None, ShipRegion: None, ShipZip: None, ShipCountry: None, AmountTotal:  [None-->] 684.0000000000, Country: None, City: None, Ready: None, OrderDetailCount:  [None-->] 1, CloneFromOrder: 10643  row: 0x109489290  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:22,083 - logic_logger - INF
........Customer[ALFKI] {Update - Adjusting Customer: Balance} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 2786.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11, Client_id: 1  row: 0x1096b8f90  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:22,084 - logic_logger - INF
........Customer[ALFKI] {Constraint Failure: balance (2786.00) exceeds credit (2300.00)} Id: ALFKI, CompanyName: Alfreds Futterkiste, ContactName: Maria Anders, ContactTitle: Sales Representative, Address: Obere Str. 57A, City: Berlin, Region: Western Europe, PostalCode: 12209, Country: Germany, Phone: 030-0074321, Fax: 030-0076545, Balance:  [2102.0000000000-->] 2786.0000000000, CreditLimit: 2300.0000000000, OrderCount: 16, UnpaidOrderCount: 11, Client_id: 1  row: 0x1096b8f90  session: 0x10948bbd0  ins_upd_dlt: upd - 2023-07-16 19:02:22,085 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
## Feature: Salary Change  
  
&nbsp;
&nbsp;
### Scenario: Audit Salary Change
&emsp;  Scenario: Audit Salary Change  
&emsp;&emsp;    Given Employee 5 (Buchanan) - Salary 95k  
&emsp;&emsp;    When Patch Salary to 200k  
&emsp;&emsp;    Then Salary_audit row created  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Audit Salary Change
   
Observe the logic log to see that it creates audit rows:

1. **Discouraged:** you can implement auditing with events.  But auditing is a common pattern, and this can lead to repetitive, tedious code
2. **Preferred:** approaches use [extensible rules](https://github.com/valhuber/LogicBank/wiki/Rule-Extensibility#generic-event-handlers).

Generic event handlers can also reduce redundant code, illustrated in the time/date stamping `handle_all` logic.

This is due to the `copy_row` rule.  Contrast this to the *tedious* `audit_by_event` alternative:

<figure><img src="https://github.com/valhuber/ApiLogicServer/wiki/images/behave/salary_change.png?raw=true"></figure>

> **Key Takeaway:** use **extensible own rule types** to automate pattern you identify; events can result in tedious amounts of code.



&nbsp;
&nbsp;


**Rules Used** in Scenario: Audit Salary Change
```
  
```
**Logic Log** in Scenario: Audit Salary Change
```

Logic Phase:		BEFORE COMMIT(session=0x1096bab90)          						 - 2023-07-16 19:02:22,124 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x1096bab90) (sqlalchemy before_flush)			 - 2023-07-16 19:02:22,125 - logic_logger - INF
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: Employee/buchanan.jpg, EmployeeType: Commissioned, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None, UnionId: None, Dues: None  row: 0x1096bbed0  session: 0x1096bab90  ins_upd_dlt: upd - 2023-07-16 19:02:22,125 - logic_logger - INF
..Employee[5] {BEGIN Copy to: EmployeeAudit} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: Employee/buchanan.jpg, EmployeeType: Commissioned, Salary:  [95000.0000000000-->] 200000, WorksForDepartmentId: 3, OnLoanDepartmentId: None, UnionId: None, Dues: None  row: 0x1096bbed0  session: 0x1096bab90  ins_upd_dlt: upd - 2023-07-16 19:02:22,127 - logic_logger - INF
....EmployeeAudit[None] {Insert - Copy EmployeeAudit} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: None  row: 0x10948a750  session: 0x1096bab90  ins_upd_dlt: ins - 2023-07-16 19:02:22,128 - logic_logger - INF
....EmployeeAudit[None] {early_row_event_all_classes - handle_all sets 'Created_on} Id: None, Title: Sales Manager, Salary: 200000, LastName: Buchanan, FirstName: Steven, EmployeeId: None, CreatedOn: 2023-07-16 19:02:22.128532  row: 0x10948a750  session: 0x1096bab90  ins_upd_dlt: ins - 2023-07-16 19:02:22,128 - logic_logger - INF
Logic Phase:		COMMIT(session=0x1096bab90)   										 - 2023-07-16 19:02:22,128 - logic_logger - INF

```
</details>
  
&nbsp;
&nbsp;
### Scenario: Manage ProperSalary
&emsp;  Scenario: Manage ProperSalary  
&emsp;&emsp;    Given Employee 5 (Buchanan) - Salary 95k  
&emsp;&emsp;    When Retrieve Employee Row  
&emsp;&emsp;    Then Verify Contains ProperSalary  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Manage ProperSalary
   
Observe the use of `old_row
`
> **Key Takeaway:** State Transition Logic enabled per `old_row`



&nbsp;
&nbsp;


**Rules Used** in Scenario: Manage ProperSalary
```
```
**Logic Log** in Scenario: Manage ProperSalary
```

Logic Phase:		BEFORE COMMIT(session=0x1096f7210)          						 - 2023-07-16 19:02:22,269 - logic_logger - DEBU
```
</details>
  
&nbsp;
&nbsp;
### Scenario: Raise Must be Meaningful
&emsp;  Scenario: Raise Must be Meaningful  
&emsp;&emsp;    Given Employee 5 (Buchanan) - Salary 95k  
&emsp;&emsp;    When Patch Salary to 96k  
&emsp;&emsp;    Then Reject - Raise too small  
<details markdown>
<summary>Tests - and their logic - are transparent.. click to see Logic</summary>


&nbsp;
&nbsp;


**Logic Doc** for scenario: Raise Must be Meaningful
   
Observe the use of `old_row
`
> **Key Takeaway:** State Transition Logic enabled per `old_row`



&nbsp;
&nbsp;


**Rules Used** in Scenario: Raise Must be Meaningful
```
  Employee  
    1. Constraint Function: <function declare_logic.<locals>.raise_over_20_percent at 0x108dacd60>   
  
```
**Logic Log** in Scenario: Raise Must be Meaningful
```

Logic Phase:		BEFORE COMMIT(session=0x1096f4a50)          						 - 2023-07-16 19:02:22,315 - logic_logger - DEBU
Logic Phase:		ROW LOGIC(session=0x1096f4a50) (sqlalchemy before_flush)			 - 2023-07-16 19:02:22,315 - logic_logger - INF
..Employee[5] {Update - client} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: Employee/buchanan.jpg, EmployeeType: Commissioned, Salary:  [95000.0000000000-->] 96000, WorksForDepartmentId: 3, OnLoanDepartmentId: None, UnionId: None, Dues: None  row: 0x1096f51d0  session: 0x1096f4a50  ins_upd_dlt: upd - 2023-07-16 19:02:22,315 - logic_logger - INF
..Employee[5] {Constraint Failure: Buchanan needs a more meaningful raise} Id: 5, LastName: Buchanan, FirstName: Steven, Title: Sales Manager, TitleOfCourtesy: Mr., BirthDate: 1987-03-04, HireDate: 2025-10-17, Address: 14 Garrett Hill, City: London, Region: British Isles, PostalCode: SW1 8JR, Country: UK, HomePhone: (71) 555-4848, Extension: 3453, Notes: Steven Buchanan graduated from St. Andrews University, Scotland, with a BSC degree in 1976.  Upon joining the company as a sales representative in 1992, he spent 6 months in an orientation program at the Seattle office and then returned to his permanent post in London.  He was promoted to sales manager in March 1993.  Mr. Buchanan has completed the courses 'Successful Telemarketing' and 'International Sales Management.'  He is fluent in French., ReportsTo: 2, PhotoPath: Employee/buchanan.jpg, EmployeeType: Commissioned, Salary:  [95000.0000000000-->] 96000, WorksForDepartmentId: 3, OnLoanDepartmentId: None, UnionId: None, Dues: None  row: 0x1096f51d0  session: 0x1096f4a50  ins_upd_dlt: upd - 2023-07-16 19:02:22,316 - logic_logger - INF

```
</details>
  
&nbsp;&nbsp;  
behave_run.py completed at July 16, 2023 19:02:2  