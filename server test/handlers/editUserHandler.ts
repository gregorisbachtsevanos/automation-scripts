// getUserHandler.ts
import { Request, Response } from "express";
import UserService from "../services/userService";

const userService = new UserService();

export const editUserHandler = async (
	req: Request,
	res: Response
): Promise<void> => {
	const userId = req.params.userId;
	try {
		const user = await userService.getUserById(userId);
		if (user) {
			res.status(200).json(user);
		} else {
			res.status(404).json({ message: "User not found" });
		}
	} catch (error) {
		res.status(500).json({ message: "Internal Server Error" });
	}
};
