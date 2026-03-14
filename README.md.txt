API Testing with Postman

Overview
 This folder holds Postman API tests for e-commerce features using the mock API service provided by 'ReqRes.in'.

Files
 postman_collection.json - Complete API test collection

How to Use

Method 1: Import into Postman
1. Open Postman
2. Click Import button on the top left corner
3. Drag & Drop postman_collection.json file
4. Click Import

Method 2: Run via Command Line
```bash
# Install Newman (requires Node.js)
npm install -g newman
# Run collection
newman run postman_collection.json
```