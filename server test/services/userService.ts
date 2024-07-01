import { IUser } from "../model/userModel";
import { v4 as uuidv4 } from "uuid";
class UserService {
	private users: IUser[]; // Example in-memory storage, replace with DB access

	constructor() {
		this.users = []; // Initialize with an empty array or fetch from DB
	}

	async getUserById(userId: string): Promise<IUser | undefined> {
		// Example: Fetch user from an in-memory array or database
		const user = this.users.find((u) => u.id === userId);
		return user;
	}

	async getUsers(): Promise<IUser | undefined> {
		// Example: Fetch users from an in-memory array or database
		const user = this.users.find((u) => u.id === userId);
		return user;
	}

	async createUser(userData: IUser): Promise<IUser> {
		// Example: Create a new user and store in an in-memory array or database
		const newUser: IUser = {
			id: uuidv4(),
			name: userData.name,
			email: userData.email,
			// other properties as needed
		};
		this.users.push(newUser); // Example: Store in-memory or save to database
		return newUser;
	}

	// Example of updating user information
	async updateUser(
		userId: string,
		updatedUserData: any
	): Promise<IUser | undefined> {
		// Example: Update user information in an in-memory array or database
		const userIndex = this.users.findIndex((u) => u.id === userId);
		if (userIndex !== -1) {
			this.users[userIndex].name =
				updatedUserData.name || this.users[userIndex].name;
			this.users[userIndex].email =
				updatedUserData.email || this.users[userIndex].email;
			// Update other properties as needed
			return this.users[userIndex];
		}
		return undefined; // User not found
	}

	// Example of deleting a user
	async deleteUser(userId: string): Promise<boolean> {
		// Example: Delete user from an in-memory array or database
		const initialLength = this.users.length;
		this.users = this.users.filter((u) => u.id !== userId);
		return this.users.length !== initialLength;
	}

	// Additional methods as needed, like fetching all users, etc.
}

export default UserService;
