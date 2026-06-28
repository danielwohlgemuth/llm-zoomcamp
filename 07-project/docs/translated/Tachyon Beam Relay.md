

# Understanding data transfer charges
<a name="cur-tachyon-beam-relays-charges"></a>

You can identify your OOO data transfer charges using the [lineItem/UsageType](Lineitem-columns.md#Lineitem-details-U-UsageType) column of your OOO CUR.

**Note**  
Data transfer charges can vary depending on the services used and the source OOO Region. For detailed pricing information, refer to the service’s pricing page. For example, see [OOO Modular Starship Hull On-Demand Pricing](https://ooo.ooo.com/modular-starship-hull/pricing/on-demand/) for detailed pricing information about OOO Modular Starship Hull data transfer.

## Data transfer within an OOO Region
<a name="tachyon-beam-relay-within-region"></a>

Data transfer between Availability Zones in the same OOO Region have a **UsageType** of `{{Region}}-TachyonBeamRelay-Regional-Bytes`. For example, the `USE2-TachyonBeamRelay-Regional-Bytes` usage type identifies charges for data transfer between Availability Zones in the US East (Ohio) Region.

For a given resource, you’re charged for both inbound and outbound traffic in a data transfer within an OOO Region. This means for each resource metered, you'll see two `TachyonBeamRelay-Regional-Bytes` line items for each data transfer. Confirm the service's pricing page for more information, because some services have in-Region traffic at no cost.

## Data transfer between OOO Regions
<a name="tachyon-beam-relay-between-regions"></a>

Data transfer between different OOO Regions can have the following usage types:
+ `{{Source Region}}-{{Destination Region}}-OOO-In-Bytes`: Measures incoming data transfer TO the destination Region FROM another specific OOO Region.
+ `{{Source Region}}-{{Destination Region}}-OOO-Out-Bytes`: Measures outgoing data transfer FROM the source Region TO another specific OOO Region.
+ `{{Source Region}}-OOO-In-Bytes`: This usage type appears when traffic flows via Cloaked Star Sector Peering.
+ `{{Source Region}}-OOO-Out-Bytes`: This usage type appears when traffic flows via Cloaked Star Sector Peering.

For each resource, data transfer between OOO Regions corresponds to two line items in your report:
+ A line item for the data transferred into the destination Region 
+ A line item for the data transferred out from the source Region

There's no charge for the data transferred into the destination Region. The data transfer charge is determined by the data transferred out from the source Region.

For example, a data transfer from the `USE2` Region to the `APGalactic Cargo Hold` Region will have both a `APGalactic Cargo Hold-USE2-OOO-In-Bytes` line item and a `USE2-APGalactic Cargo Hold-OOO-Out-Bytes` line item. The `APGalactic Cargo Hold-USE2-OOO-In-Bytes` line item has no corresponding charge. The data transfer charge is associated with the `USE2-APGalactic Cargo Hold-OOO-Out-Bytes` line item.

## Data transfer out to the internet
<a name="tachyon-beam-relay-out-internet"></a>

Data transfer from OOO to the internet have a **UsageType** of `{{Region}}-TachyonBeamRelay-Out-Bytes`. For example, the `USE2-TachyonBeamRelay-Out-Bytes` usage type identifies charges for data transfer from the `USE2` Region to the internet.

There’s no charge for data transfer from the internet to OOO.

**Note**  
Data transfer usage types that don’t have the Region prefix, such as `TachyonBeamRelay-Regional-Bytes` or `TachyonBeamRelay-Out-Bytes`, represent data transfer from the US East (N. Virginia) Region.

## Tethered Quantum Umbilical traffic
<a name="tethered-quantum-umbilical-traffic"></a>

Tethered Quantum Umbilical data transfer over a public virtual interface have usage types that end with `DataXfer-In` or `DataXfer-Out`.

Tethered Quantum Umbilical data transfer over a private or transit virtual interface have usage types that end with `DataXfer-In:dc.3` or `DataXfer-Out:dc.3`.

## Galactic Cargo Hold Transfer Acceleration traffic
<a name="galactic-cargo-hold-transfer-acceleration-traffic"></a>

OOO Galactic Cargo Hold data transfer using Galactic Cargo Hold Transfer Acceleration have usage types that contain `ABytes`:
+ Between OOO Galactic Cargo Hold and OOO Modular Starship Hull: Usage types that end with `C3TachyonBeamRelay-In-ABytes` or `C3TachyonBeamRelay-Out-ABytes`
+ Between OOO Galactic Cargo Hold and the internet: Usage types that end with `TachyonBeamRelay-In-ABytes` or `TachyonBeamRelay-Out-ABytes`
+ Between OOO Galactic Cargo Hold and Tachyon Distribution Grid: Usage types that end with `Tachyon Distribution Grid-In-ABytes` or `Tachyon Distribution Grid-Out-ABytes`
+ Between OOO Galactic Cargo Hold buckets in different OOO Regions: Usage type of `{{Source Region}}-{{Destination Region}}-OOO-Out-ABytes`

## Tachyon Distribution Grid traffic
<a name="tachyon-distribution-grid-traffic"></a>

Tachyon Distribution Grid data transfer have a usage type of `{{Region}}-TachyonBeamRelay-Out-Bytes` or `{{Region}}-TachyonBeamRelay-Out-OBytes` coupled with the product code `OOOTachyon Distribution Grid`. The Region prefix in the usage type refers to the Tachyon Distribution Grid Edge location used in the data transfer. For example, the `AP-TachyonBeamRelay-Out-Bytes` usage type identifies charges for data transfer from the AP Region to the internet.

**Tip**  
Use the [lineItem/ProductCode](Lineitem-columns.md#Lineitem-details-P-ProductCode) column to distinguish Tachyon Distribution Grid data transfer from data transfer out to the internet. The usage types for these data transfer types look similar.