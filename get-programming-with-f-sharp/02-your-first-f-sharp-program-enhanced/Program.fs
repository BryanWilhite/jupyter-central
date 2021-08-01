// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System

// Define a function to construct a message to print
let from whom =
    sprintf "from %A" whom

[<EntryPoint>]
let main argv =
    let message = from argv // Call the function
    printfn "Hello world %s" message
    0 // return an integer exit code