markdown
# Amazon Scraper Component

## 1. Component Name
AmazonScraper

## 2. Description
The AmazonScraper component is designed to retrieve product information from Amazon by searching for a given product name. It uses an external Amazon API to perform the search and returns a list of products found along with their relevant details.

## 3. Input and Output Models
### Input Model
AmazonScraperInputDict - A Pydantic BaseModel with the following field:
- `product_name`: The name of the product to search for on Amazon.

### Output Model
AmazonScraperOutputDict - A Pydantic BaseModel with the following field:
- `product_results`: A list of dictionaries containing product details, including the product URL, name, and ASIN.

Both models provide built-in validation and serialization methods through the Pydantic library.

## 4. Parameters
- `api_key` (Optional[str]): The API key used for making requests to the external Amazon API.
- `search_results_limit` (int): The maximum number of search results to retrieve from the Amazon API.

These parameters are loaded from a configuration file and can be accessed through the `self.api_key` and `self.search_results_limit` properties.

## 5. Transform Function
The transform() method takes an AmazonScraperInputDict object as input and performs the following steps:
1. Constructs the search URL based on the provided product name and search_results_limit.
2. Creates a header with the Content-Type, Authorization, and Bearer token for the Amazon API request.
3. Makes a request to the Amazon API and checks the status code for success. If the status code is not 200, it raises an exception with a descriptive error message.
4. Processes the received search results, extracting the relevant product information (URL, name, and ASIN), and creates a list of dictionaries.
5. Returns an AmazonScraperOutputDict object containing the product_results list.

## 6. External Dependencies
- `os` (Python built-in): Used to access environment variables for API key.
- `yaml`: Used to load component configurations (e.g., parameters) from a file.
- `dotenv`: Provides functionality to load environment variables from a .env file.
- `fastapi`: Used to create an endpoint for the component's transform function.
- `pydantic`: Provides functionality for data validation and serialization through BaseModel classes.
- `requests`: Used to make HTTP requests to the external Amazon API.

## 7. API Calls
The AmazonScraper component makes a GET request to the external Amazon API, specifically the `/search` endpoint. The request includes the product name as a query parameter and uses the Authorization and Bearer token headers. The purpose of this API call is to retrieve product information based on the search query.

## 8. Error Handling
Error handling in the component is done mainly through exceptions. If the Amazon API call's status code is not 200, an exception is raised with a descriptive error message informing the user of the issue with the API call.

## 9. Examples
To use the AmazonScraper component in a Yeager Workflow, create an instance of the component and call its transform() function with an AmazonScraperInputDict object containing the desired product name. Make sure the Amazon API key is set in the environment (either through a .env file or other means) and that the component configuration file points to the correct parameter values.

Example usage:

