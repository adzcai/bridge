// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
// and set the environment variables. See http://twil.io/secure
export const accountSid = process.env.TWILIO_ACCOUNT_SID;
export const authToken = process.env.TWILIO_AUTH_TOKEN;
export const verifySid = process.env.TWILIO_VERIFY_SID;
export const client = require('twilio')(accountSid, authToken);
