// createUserHandler.ts
import { Request, Response } from "express";
import UserService from "../services/userService";

const userService = new UserService();

export const createUser = async (
	req: Request,
	res: Response
): Promise<void> => {
	const userData = req.body;
	try {
		const newUser = await userService.createUser(userData);
		res.status(201).json(newUser);
	} catch (error) {
		res.status(500).json({ message: "Internal Server Error" });
	}
};
