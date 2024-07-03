// Import necessary modules
import nodemailer from 'nodemailer';
import schedule from 'node-schedule';

// Email account credentials
const senderEmail = "your_email@example.com";
const senderPassword = "your_password";
const receiverEmail = "receiver_email@example.com";

// Create a transporter
const transporter = nodemailer.createTransport({
    service: 'gmail', // Use your email service
    auth: {
        user: senderEmail,
        pass: senderPassword,
    },
});

// Email options
const mailOptions = {
    from: senderEmail,
    to: receiverEmail,
    subject: 'Daily Report',
    text: `
    Hi,

    This is your daily report.

    Best regards,
    Your Automation Script
    `,
};

// Function to send the email
const sendEmail = () => {
    transporter.sendMail(mailOptions, (error, info) => {
        if (error) {
            return console.log(`Error: ${error}`);
        }
        console.log(`Email sent: ${info.response}`);
    });
};

// Schedule the email to be sent daily at 8 AM
schedule.scheduleJob('0 8 * * *', () => {
    console.log('Sending daily email...');
    sendEmail();
});

console.log('Email scheduler started. An email will be sent daily at 8 AM.');
