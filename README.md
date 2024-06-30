# Custom-Search-Engine

## Steps to Set Up Google Custom Search JSON API:

1. Create a Google Custom Search Engine (CSE):

   - Go to Google [Custom Search Engine](https://programmablesearchengine.google.com/about/).
   - Click on "New search engine".
   - Enter any website in the "Sites to search" field (e.g., example.com). This is just to create the engine; you can later configure it to search the entire web.
   - Name your search engine and click "Create".

2. Configure the Search Engine:

   - After creating the search engine, go to the CSE control panel.
   - In the "Sites to search" section, change it to "Search the entire web".
   - Note down the cx (Custom Search Engine ID) from the CSE control panel. This is required for the API requests.

   > [!NOTE]
   > your CSE code sample :

   ```js
   <script async src="https://cse.google.com/cse.js?cx=YOUR_SEARCH_ENGINE_ID"></script>
    <div class="gcse-search"></div>
   ```

3. Enable the Custom Search JSON API:

   - Go to the [Google Cloud Console](https://console.google.com).
   - Create a new project or select an existing project.
   - Go to the "Library" section in the left sidebar.
   - Search for "Custom Search API" and enable it.

4. Obtain the API Key:

   -In the Google Cloud Console, go to "Credentials" in the left sidebar.

   - Click on "Create credentials" and select "API key".
   - Copy the generated API key. This will be used for authentication in your API requests.

## Summary of Required Information:

1. API Key: This is used for authenticating your API requests.
2. Custom Search Engine ID (cx): This identifies your custom search engine configuration.
