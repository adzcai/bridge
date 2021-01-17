import { client } from '../../shared/twilio';

export default async function handle(req, res) {
  const phone = req.body.phone;

  const validationRequest = await client.validationRequests.create({
    phoneNumber: phone,
    friendlyName: 'Alex\'s Phone',
  });

  console.log(validationRequest);

  res.send('Done');
}
