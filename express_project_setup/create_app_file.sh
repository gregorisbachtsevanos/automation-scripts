# Rewrite www.ts file
APP='import createError from 'http-errors';
import express from 'express';
import cookieParser from 'cookie-parser';
import logger from 'morgan';
import cors from 'cors'

import authRouter from './routes/auth_router.js';
import emailsRouter from './routes/emails_router.js';
import languageRouter from './routes/language_router.js';
import projectsRouter from './routes/projects_router.js';
import userRouter from './routes/user_router.js';

import { CLIENT_URL, INDEX_ENDPOINT } from './constants/variables.js';
import serverErrorHandler from './utils/serverErrorHandler.js';

import './config/index.js'
import multer from 'multer'

var app = express();

app.use(cors(CLIENT_URL));
app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({
  extended: true,
})
);
app.use(cookieParser());

app.use(INDEX_ENDPOINT, authRouter);
app.use(INDEX_ENDPOINT, userRouter);
app.use(INDEX_ENDPOINT, emailsRouter);
app.use(INDEX_ENDPOINT, languageRouter);
app.use(INDEX_ENDPOINT, projectsRouter);

// catch 404 and forward to error handler
// app.use(function (req, res, next) {
//   next(createError(404));
// });

app.all('*', (err, req, res, next) => {
  next(new serverErrorHandler(err, 500));
})

app.use((err, req, res, next) => {
  const { status = 500, message = 'Something went wrong' } = err;
  // console.log(err)
  // if (err instanceof multer.MulterError) {
  //   res.statusCode = 400;
  //   res.send(err.code);
  // } else if (err) {
  //   if (err.message === "FILE_MISSING") {
  //     res.statusCode = 400;
  //     res.send("FILE_MISSING");
  //   } else {
  //     res.statusCode = 500;
  //     res.send("GENERIC_ERROR");
  //   }
  // }
  res.status(status).json(message)
})

// error handler
app.use((err, req, res, next) => {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  res.status(err.status || 500);
});

export default app;
'

create_json_file "app.ts" "$APP"

echo "App file created successfully."
