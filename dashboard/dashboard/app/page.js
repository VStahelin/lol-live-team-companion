"use client";
import React, {useEffect, useState} from 'react';


export default function Home() {
    const [messages, setMessages] = useState([]);


    useEffect(() => {
        const eventSource = new EventSource('http://127.0.0.1:8000/data_stream/events');
        eventSource.onmessage = (event) => {
            const data = JSON.parse(event.data);
            setMessages([...messages, event.data]);
        };

        eventSource.onerror = (error) => {
            console.error('SSE error:', error);
        };
        return () => {
            eventSource.close();
        };
    }, [messages]);



    return (
        <main className="flex min-h-screen flex-col items-center justify-between p-24">
            <h1 className="text-6xl font-bold text-center">
                Welcome to Team Companion
            </h1>
            <div>
                <p>Received Messages:</p>
                <ul>
                    {messages.map((message, index) => (
                        <li key={index}>{message}</li>
                    ))}
                </ul>
            </div>
        </main>
    )
}
