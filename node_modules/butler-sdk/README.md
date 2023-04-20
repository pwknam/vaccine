# Butler
Welcome to [Butler's Javascript and Typescript SDK](https://butlerlabs.ai)

      Butler APIs are built on top of the OpenAPI 3.0 standard, and the SDK provides convenience
      functions to make programming easier

## Installation & Usage
### npm install

```sh
npm install butler-sdk
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```typescript

import { Butler } from 'butler-sdk';
// Get API Key from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#get-your-api-key
const apiKey = '<api-key>'
// Get Queue ID from https://docs.butlerlabs.ai/reference/uploading-documents-to-the-rest-api#go-to-the-model-details-page
const queueId = '<queue_id>'
const file = fs.createReadStream('test.pdf');

// Create client
const client = new Butler(apiKey)

client.extractFile(queueId, file).then((x) => {
  console.log(x);
});
```

## Maintain
### Regenerate code to reflect latest API Spec
```sh
openapi-generator generate -i https://app.butlerlabs.ai/api/docs-json -g typescript-axios --package-name butler
```

### Test
```sh
API_KEY="api-key" QUEUE_ID="queue-id" yarn run ts-node test.ts
```
