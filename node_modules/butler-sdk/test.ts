import { Butler } from "./client";
import * as fs from 'fs';

const apiKey = process.env.API_KEY || ''
const client = new Butler(apiKey)
const queueId = process.env.QUEUE_ID || ''
const file = fs.createReadStream('test.pdf');
client.extractDocument(queueId, file).then((x) => {
  console.log(x);
})
