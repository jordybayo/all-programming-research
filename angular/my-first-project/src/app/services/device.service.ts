import { Subject } from 'rxjs';

export class DevicesService{
    deviceSubject = new Subject<any[]>();
    private devices = [
        {
            id: 1,
            name : 'machine a laver',
            status : 'eteint'
        },
        {
            id: 2,
            name : 'television',
            status : 'allume'
        },
        {
            id: 3,
            name : 'Ordinateur',
            status : 'allume'
        }
    ];

    emitDeviceSubject(){
        this.deviceSubject.next(this.devices.slice());
    }

    getDeviceById(id: number){
        const device = this.devices.find(
            (deviceObject)=>{
                return deviceObject.id === id;
            }
        );
        return device;
    }

    switchOnAll(){
        for(let device of this.devices){
            device.status = 'allume';
        }
        this.emitDeviceSubject();
    }

    switchOffAll(){
        for(let device of this.devices){
            device.status = 'eteint';
        }
        this.emitDeviceSubject();
    }

    switchOnOne(index: number){
        this.devices[index].status = 'allume';
        this.emitDeviceSubject();
    }

    switchOffOne(index: number){
        this.devices[index].status = 'eteint';
        this.emitDeviceSubject();
    }

    addDevice(name: string, status : string){
        const deviceObject = {
            id:0,
            name: '',
            status: '',
        };
        deviceObject.name = name;
        deviceObject.status = status;
        deviceObject.id = this.devices[(this.devices.length - 1)].id + 1;
        this.devices.push(deviceObject);
        this.emitDeviceSubject();
    }
}