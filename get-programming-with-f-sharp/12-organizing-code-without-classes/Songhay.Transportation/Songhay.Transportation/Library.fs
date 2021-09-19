namespace Songhay.Transportation

type Destinations =
    | Home = 'h'
    | Office = 'o'
    | Stadium = 's'
    | GasStation = 'g'

module Utility =

    let getDistance destination =
        if destination = Destinations.Home then 25
        elif destination = Destinations.Office then 50
        elif destination = Destinations.Stadium then 25
        elif destination = Destinations.GasStation then 10
        else failwith "Unknown destination!"

    let calculateRemainingPetrol currentPetrol distance =
        let remainingPetrol = currentPetrol - distance
        if remainingPetrol > 0 then remainingPetrol
        else failwith "Oops! You’ve run out of petrol!"

    let driveTo destination petrol =
        let distance = getDistance destination
        let remainingPetrol = calculateRemainingPetrol petrol distance
        if destination = Destinations.GasStation then remainingPetrol + 50
        else remainingPetrol
