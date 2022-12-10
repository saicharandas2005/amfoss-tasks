﻿using System;
using System.Net;
using System.Net.Sockets;
using System.Text;
// check whether all required namespaces are imported
public class SynchronousSocketListener
{   
     // check the main function
    public static int Main(String[] args)
    {
        StartListening();
        return 0;
    }

    // Incoming data from the client.  
    public static string data = null;

    public static void StartListening()
    {
        // Data buffer for incoming data.  
        byte[] bytes = new Byte[1024];

        // Establish the local endpoint for the socket.  
        // Dns.GetHostName returns the name of the
        // host running the application.  
        IPHostEntry ipHostInfo = Dns.GetHostEntry(Dns.GetHostName());
        IPAddress ipAddress = ipHostInfo.AddressList[0];
        IPEndPoint localEndPoint = new IPEndPoint(ipAddress, 11000);


        // Bind the socket to the local endpoint and
        // listen for incoming connections.
        Socket listener = new Socket(ipAddress.AddressFamily, SocketType.Stream, ProtocolType.Tcp);
        

        string fileName = "file.json";
        try
        {
            // Start listening for connections.  
            listener.Bind(localEndPoint);
            listener.Listen(10);



            while (true)
            {
                Console.WriteLine("Waiting for a connection...");
                // Program is suspended while waiting for an incoming connection.  
                Socket handler = listener.Accept();
                string data = null;
                bytes = new byte[1024];
                
                Console.WriteLine("Socket connected to {0}", handler.RemoteEndPoint.ToString());
                // An incoming connection needs to be processed.  
                // check if the varibale is defined or not also even correctly defined
                int bytesRec = handler.Receive(bytes);
                data += Encoding.ASCII.GetString(bytes, 0, bytesRec);  
                
                Console.WriteLine("Text received : {0}", data);
                string[] dataArr = data.Split(",");
                string name = dataArr[0];
                string intrests = dataArr[1];
                string mail = dataArr[2];
                string jsonData = "{ \"name\": \"" + name + "\", \"intrests\": \"" + intrests + "\", \"mail\": \"" + mail + "\" }";
                Console.WriteLine("Name: {0}", name);
                Console.WriteLine("Intrests: {0}", intrests);
                Console.WriteLine("Email: {0}", mail);

                 
                if (true)
                {
                    using (StreamWriter sw = File.AppendText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
                else
                {
                    using (StreamWriter sw = File.CreateText(fileName))
                    {
                        sw.WriteLine(jsonData);
                    }
                }
            handler.Shutdown(SocketShutdown.Both);
            handler.Close();
            }


        }
        catch (Exception e)
        {
            Console.WriteLine(e.ToString());
        }

        Console.WriteLine("\nPress ENTER to continue...");
        Console.Read();

    }

}