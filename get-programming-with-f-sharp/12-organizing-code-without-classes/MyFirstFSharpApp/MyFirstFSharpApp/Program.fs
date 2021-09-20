// This file should be the last file declared in the `*.fsproj`
open System
open MyFirstFSharpApp.Domain
open MyFirstFSharpApp.Operations

[<EntryPoint>]
let main argv =
    let joe = { FirstName = "Joe"; LastName = "Bloggs"; Age = 21 }
    if joe |> isOlderThan 18 then Console.WriteLine $"{joe |> getInitials} is an adult!"
    else Console.WriteLine $"{joe |> getInitials} is a child."

    0 // return an integer exit code