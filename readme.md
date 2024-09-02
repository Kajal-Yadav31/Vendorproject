# Vendor Performance Tracking System

This project is a vendor performance tracking system built with Django and Django REST Framework. It tracks and analyzes vendor performance metrics such as on-time delivery rate, quality rating average, average response time, and fulfillment rate.

## Getting Started
### Clone the Repository
- First, clone the repository to your local machine:
git clone https://github.com/Kajal-Yadav31/Vendorproject.git

- Change directory to the project:
cd Vendorproject


## API Endpoints

### Vendor Endpoints
- **List/Create Vendors**

URL: /vendor/
Method: GET or POST
Description:
GET: Retrieve a list of all vendors.
POST: Create a new vendor.

- **Retrieve/Update/Delete Vendor**
URL: /vendor/<int:vendor_id>/
Method: GET, PUT, PATCH, or DELETE
Description: Retrieve, update, or delete a specific vendor.

- **Retrieve Vendor Performance**

URL: /vendors/<int:vendor_id>/performance/
Method: GET
Description: Retrieve current and historical performance metrics for a specific vendor.
Purchase Order Endpoints

- **List/Create Purchase Orders**

URL: /purchase_orders/
Method: GET or POST
Description: Retrieve a list of all purchase orders or create a new purchase order.

- **Retrieve/Update/Delete Purchase Order**

URL: /purchase_orders/<int:po_id>/
Method: GET, PUT, PATCH, or DELETE
Description: Retrieve, update, or delete a specific purchase order.

- **Acknowledge Purchase Order**

URL: /purchases/<int:po_id>/acknowledge/
Method: POST
Description: Acknowledge a purchase order, updating the acknowledgment date and recalculating the average response time.

**If you encounter any issues or have questions about this project, please feel free to contact me. I'm here to help!**

You can reach out to me via:

Email: kajalyadav070496@gmail.com

LinkedIn: https://www.linkedin.com/in/kajal-yadav31/

GitHub: https://github.com/Kajal-Yadav31

Resume:
[My_Resume-Kajal Yadav.pdf](https://github.com/user-attachments/files/16837484/My_Resume-Kajal.Yadav.pdf)
