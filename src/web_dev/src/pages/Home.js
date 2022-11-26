import React, {useRef, useState, useEffect, useImperativeHandle, useId} from "react";
import WSClient from "../components/wsClient";

const Home = () => {

    const [receivedMessage, setReceivedMessage] = useState("");

    const wsClientRef = useRef();

    const sendMessageHandlerStart = () => {
        wsClientRef.current.sendMessage("start");
    };

    const sendMessageHandlerStop = () => {
        wsClientRef.current.sendMessage("stop");
    };

    const sendMessageHandlerStatus = () => {
        wsClientRef.current.sendMessage("status");
    };

    // this method is called from the websocket onmessage
    const renderMessage = (message) => {
        console.log(" in rendering message ");
        setTimeout(
            () => {
                console.log(" right before setReceivedMessage ");
                setReceivedMessage(message);
            },
            0
        );
        console.log(" this is callable ", message);
    };

    useEffect( () => {
        wsClientRef.current.registerClient(renderMessage);
        const defaultMessage = JSON.parse('{"message": "default"}');
        setReceivedMessage(defaultMessage.message);
    }, []);

    return (
        <React.Fragment>

            <WSClient ref={wsClientRef} />;
                        
            <div className="mainContainer"> Home of the components </div>

            <div>message: { receivedMessage }</div>

            <button type="button" onClick={sendMessageHandlerStart}> start </button>  

            <button type="button" onClick={sendMessageHandlerStop}> stop </button>  

            <button type="button" onClick={sendMessageHandlerStatus}> status </button>  

        </React.Fragment>
    );
}

export default Home;