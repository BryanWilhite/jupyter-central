// This file should be the last file declared in the `*.fsproj`
open System
open MyFirstFSharpApp.Domain
open MyFirstFSharpApp.Operations

[<EntryPoint>]
let main argv =
    let joe = { FirstName = "joe"; LastName = "bloggs"; Age = 21 }
    if joe |> isOlderThan 18 then Console.WriteLine $"{joe.FirstName} is an adult!"
    else Console.WriteLine $"{joe.FirstName} is a child."
    0 // return an integer exit code