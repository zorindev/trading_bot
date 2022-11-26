import React, {Component, useState, useEffect, useImperativeHandle} from "react";
import * as uuid from 'uuid'
import { w3cwebsocket as W3CWebSocket } from "websocket";

const WSClient = React.forwardRef( (props, ref) => {

    const [sttWSClient, setWSClient] = useState(null);
    const [sttMessage, setMessage] = useState(null);
    const [sttClients, setClientList] = useState([]);
    
    useEffect( () => {
        console.log("setting up ws client");

        if(sttWSClient === null) {

            console.log(" websocket was null so setting up new ws client ");
            const __wsClient = new W3CWebSocket('ws://localhost:8888/websocket');

            __wsClient.onopen = () => {
                console.log(" ws client opened");

                let __message = "status";
                let message = {
                    id: uuid.v4(),
                    timestamp: Date.now(),
                    value: __message
                };
                __wsClient.send(JSON.stringify(message));
            }; 

            __wsClient.onclose = () => {
                console.log(" ws client closed ");
            };

            __wsClient.onmessage = (__message) => {
                console.log(" ws client message ", __message);
                setMessage(__message.data);

                if(sttClients) {
                    console.log(" sttClient is ", sttClients );
                    sttClients.map( (clnt) => {
                        clnt(__message.data);
                    });
                } else {
                    console.log("sttClients are not set ");
                }
            };

            setWSClient(__wsClient);

        } else {
            console.log(" web socket was already created ");
        }

    }, []);

    const sendMessage = (__message) => {
        console.log("sending message: ", __message);
        let message = {
            id: uuid.v4(),
            timestamp: Date.now(),
            value: __message
        };
        sttWSClient.send(JSON.stringify(message));
    };

    const getMessage = () => {
        console.log(" getting message: ", sttMessage);
        return sttMessage;
    };

    const registerClient = (clnt) => {
        console.log(" registering client: ", clnt);
        const __sttClients = sttClients.push(clnt);
        setClientList(__sttClients);
        console.log(" sttClients: ", sttClients);
    };

    useImperativeHandle(ref, () => ({
        sendMessage,
        getMessage,
        registerClient
    }));
    
    return (
        <React.Fragment />
    );
});

export default WSClient;