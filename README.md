    # WAREHOUSE MANAGEMENT - WEBSITE FOR HELPING MANAGE WAREHOUSE INVENTORY
    #### Video Demo:  <https://www.youtube.com/watch?v=7eCds972jDY>

    #### Description:
    My family owns a fairly large company that imports and exports agricultural products (oranges, apples, kiwis, lemons, etc.), so for my final project in CS50, I decided to create a webpage that could make it easier for them to view and update their inventory. The basic idea is, since the main warehouse is in a small town Opuzen, to have one admin located in Opuzen and several other users located in other smaller warehouses around Croatia.

    The administrator has the ability to add and delete individual products. In addition to entering the name of the product, the admin also enters its quantity of products expressed in kilograms.

    When an individual product has been added to the database, the name of the product, its quantity, and the time of entry of that product into the database are displayed on the "Warehouse status" page.

    If the user is logged in as an administrator, then there is a "delete" button next to each product, so that if it was an incorrect entry, or there was a change in the quantity of the product, the administrator can click on the previously mentioned button and thus delete the unwanted entry.

    The administrator can then go to "update status" and add the desired (new correct) value of the deleted product there. Of course, he can also add all necessary new products and their quantities. New products and their quantities will be added to the database and immediately visible if you go to "Warehouse status".

    If the user is logged in as a user and not as an administrator, then in the header there is only "Warehouse status" where the administrator was also offered "Update status".
    This is of course for the reason that we do not want any user / any employee of the company to be able to change the warehouse inventory of the company.

    For the same reason, I do not offer on the site sine up so that anyone can register to access the site and thus access sensitive data for the company.
    Therefore, I decided to hard code the administrator's name as well as the user's name and their associated passwords.

    Further, if the user is logged in as a user (and not as an administrator), then if he goes to "Warehouse status" he will see the name of the product, its quantity expressed in kilograms, as well as the date and time when the product was entered. However, unlike the administrator, the user does not have a "delete" button for any of the products in the database. The reason for this is also that we do not want any user (who is not an administrator) to be able to change the inventory quantities in the warehouse on their own (ie delete any entered product).

    This is a simple website that would greatly facilitate visibility of the inventory in the company's warehouse.

    #### Author
    Ivana Soče Govorko, MS Civile Engineering
    Zagreb, Croatia