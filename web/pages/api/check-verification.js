// import { client, verifySid } from '../../shared/twilio'

export default async function checkVerificationHandler(req, res) {
  const phone = req.body.phone;
  const code = req.body.verificationCode;
  if (!code || !phone || !/\+\d{10}/.test(phone)) {
    res.statusCode = 400;
    return res.send('Invalid code or phone number!');
  }

  try {
    // console.log('received code', code);

    // const verificationCheck = await client.verify.services(verifySid)
    //   .verificationChecks
    //   .create({ to: phone, code });

    // const status = verificationCheck.status;

    // if (status === 'approved') {
      res.statusCode = 200;
      return res.send('Approved');
    // } else {
    //   res.statusCode = 400;
    //   return res.send('Invalid code!');
    // }
  } catch (err) {
    console.error('An error occurred:', err);
    res.statusCode = 500;
    return res.send(err.message);
  }
}
