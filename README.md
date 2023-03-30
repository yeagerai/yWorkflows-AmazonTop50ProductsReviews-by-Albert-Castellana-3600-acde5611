
# AmazonTop50ProductsReviews

This Yeager Workflow takes a product name as input, searches Amazon for the top 50 products with that name, and creates a spreadsheet containing the product links and reviews for each product. The workflow consists of the following steps: 1. Receive the product name input. 2. Use an AmazonScraper Component to search Amazon for the top 50 products with the given name. 3. Extract the product links, and reviews for each product using a ProductDataExtractor Component. 4. Combine the extracted data into a structured format using the DataMerger Component. 5. Create a spreadsheet containing the product links and reviews using the SpreadsheetCreator Component.

## Initial generation prompt
a workflow that takes in a product name, scans amazon for the top 50 products with that name and creates a spreadsheet with the link and the reviews for each product

## Authors: 
- yWorkflows
- Albert Castellana#3600
        