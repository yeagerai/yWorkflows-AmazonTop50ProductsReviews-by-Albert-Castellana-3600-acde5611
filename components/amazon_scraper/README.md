
# AmazonScraper

This Component searches Amazon for the top 50 products with the provided product name. It uses the Amazon's search API to perform the search and retrieves the product URLs, names, and ASINs in the search results.

## Initial generation prompt
description: 'This Component searches Amazon for the top 50 products with the provided
  product name. It uses the Amazon''s search API to perform the search and retrieves
  the product URLs, names and ASINs in the search results.

  '
name: AmazonScraper


## Transformer breakdown
- Read the input product_name
- Call the Amazon search API with the provided product_name and api_key
- Parse the search API response
- Extract the URLs, names, and ASINs of the top search_results_limit results
- Create a list of dictionaries containing the product information
- Return the list of product dictionaries

## Parameters
[{'default_value': '', 'description': "The API key used to access Amazon's search API.", 'name': 'api_key', 'type': 'str'}, {'default_value': 50, 'description': 'The maximum number of product search results to be retrieved.', 'name': 'search_results_limit', 'type': 'int'}]

        