[<AutoOpen>]
module CommandParsing

    let isValidCommand (cmd, amt) = [ 'd'; 'w'; 'x' ] |> List.contains cmd
    let isValidAmount (cmd, amt) = Some(amt).IsSome
    let isValidCommandAndAmount (cmd, amt) =
        [
            isValidCommand
            isValidAmount
        ]
        |> List.map (fun f -> f (cmd, amt)) 
        |> List.reduce (fun previous current -> previous && current)

    let isStopCommand (cmd, amt) = cmd = 'x'
