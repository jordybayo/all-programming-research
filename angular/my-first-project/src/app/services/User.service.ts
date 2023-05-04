import { User } from '../models/User.model';
import { Subject } from 'rxjs/internal/Subject';

export class UserService{
    private users: User[] = [
        {
            firstName: 'james',
            lastName : 'smith',
            email : 'jame@smith.com',
            drinkPreference: 'Coca',
            hobbies : [
                'coder',
                'la degustation de cafe'
            ]
        },
    ];
    userSubject = new Subject<User[]>();

    emitUsers(){
        this.userSubject.next(this.users.slice());
    }

    addUser(user: User){
        this.users.push(user);
        this.emitUsers();
    }
}