
class Message {

    static instance = null;

    static getInstance() {
        if(!Message.instance) {
            Message.instance = new Message();
        } 

        return Message.instance;
    }

    sampleFunction = () => {

        console.log("message");
    }
}

export default Message.getInstance();