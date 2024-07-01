// userController.ts
import { Request, Response } from "express";
import UserService from "../services/userService";
import { getUser } from "../handlers/getUserHandler";
import { createUser } from "../handlers/createUserHandler";

class UserController {
	static createUser: any;
	static getUser: any;

	constructor(private userService: UserService) {}

	getUser = async (req: Request, res: Response): Promise<void> => {
		await getUser(req, res);
	};

	createUser = async (req: Request, res: Response): Promise<void> => {
		await createUser(req, res);
	};
}

export default UserController;
