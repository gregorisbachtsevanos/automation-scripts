import createError from "http-errors";
import express from "express";
import cookieParser from "cookie-parser";
import logger from "morgan";
import cors from "cors";
import multer from "multer";

import serverErrorHandler from "./utils/ExpressErrorHandler.js";

import "./config/index.js";
import { userRouter } from "./routes/userRouter.js";

var app = express();

app.use(cors("/domain"));
app.use(logger("dev"));
app.use(express.json());
app.use(
	express.urlencoded({
		extended: true,
	})
);
app.use(cookieParser());

app.use("/api", userRouter);

// catch 404 and forward to error handler
// app.use(function (req, res, next) {
//   next(createError(404));
// });

app.all("*", (err, req, res, next) => {
	next(new serverErrorHandler(err, 500));
});

app.use((err, req, res, next) => {
	const { status = 500, message = "Something went wrong" } = err;
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
	res.status(status).json(message);
});

// error handler
app.use((err, req, res, next) => {
	// set locals, only providing error in development
	res.locals.message = err.message;
	res.locals.error = req.app.get("env") === "development" ? err : {};

	res.status(err.status || 500);
});

export default app;
