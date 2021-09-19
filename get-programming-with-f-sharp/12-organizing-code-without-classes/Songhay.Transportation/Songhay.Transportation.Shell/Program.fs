// Learn more about F# at http://docs.microsoft.com/dotnet/fsharp

open System

open Songhay.Transportation
open Songhay.Transportation.Utility

[<EntryPoint>]
let main argv =
    let remainingPetrol =
        100
        |> driveTo Destinations.Office
        |> driveTo Destinations.Stadium
        |> driveTo  Destinations.GasStation
        |> driveTo Destinations.Home

    Console.WriteLine $"remaining petrol: {remainingPetrol}"

    0
