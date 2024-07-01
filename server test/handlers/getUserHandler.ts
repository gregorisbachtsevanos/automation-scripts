// getUserHandler.ts
import { Request, Response } from "express";
import UserService from "../services/userService";

const userService = new UserService();

export const getUsersHandler = async (
	req: Request,
	res: Response
): Promise<void> => {
	const userId = req.params.userId;
	try {
		const users = await userService.getUsers();
		if (users) {
			res.status(200).json(users);
		} else {
			res.status(404).json({ message: "User not found" });
		}
	} catch (error) {
		res.status(500).json({ message: "Internal Server Error" });
	}
};
