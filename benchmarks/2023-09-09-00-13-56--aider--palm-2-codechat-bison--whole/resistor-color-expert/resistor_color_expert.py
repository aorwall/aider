def resistor_label(colors):
  """Translates resistor color bands to a human-readable label.

  The program will take 1, 4, or 5 colors as input, and outputs the correct value,
  in ohms.

  The color bands are encoded as follows:

  - Black: 0
  - Brown: 1
  - Red: 2
  - Orange: 3
  - Yellow: 4
  - Green: 5
  - Blue: 6
  - Violet: 7
  - Grey: 8
  - White: 9

  In this exercise you will need to add tolerance to the mix.
  Tolerance is the maximum amount that a value can be above or below the main
  value.
  For example, if the last band is green, the maximum tolerance will be ±0.5%.

  The tolerance band will have one of these values:

  - Grey - 0.05%
  - Violet - 0.1%
  - Blue - 0.25%
  - Green - 0.5%
  - Brown - 1%
  - Red - 2%
  - Gold - 5%
  - Silver - 10%

  The four-band resistor is built up like this:

  | Band_1  | Band_2  | Band_3     | band_4    |
  | ------- | ------- | ---------- | --------- |
  | Value_1 | Value_2 | Multiplier | Tolerance |

  Meaning

  - orange-orange-brown-green would be 330 ohms with a ±0.5% tolerance.
  - orange-orange-red-grey would be 3300 ohms with ±0.05% tolerance.

  The difference between a four and five-band resistor is that the five-band
  resistor has an extra band to indicate a more precise value.

  | Band_1  | Band_2  | Band_3  | Band_4     | band_5    |
  | ------- | ------- | ------- | ---------- | --------- |
  | Value_1 | Value_