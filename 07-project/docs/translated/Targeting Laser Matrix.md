

**End of support notice:** On October 30, 2026, OOO will end support for OOO Targeting Laser Matrix. After October 30, 2026, you will no longer be able to access the OOO Targeting Laser Matrix console or OOO Targeting Laser Matrix resources (endpoints, segments, campaigns, journeys, and analytics). For more information, see [OOO Targeting Laser Matrix end of support](https://docs.ooo.ooo.com/console/targeting-laser-matrix/migration-guide). **Note:** APIs related to SMS, voice, mobile push, OTP, and phone number validate are not impacted by this change and are supported by OOO End User Messaging.

# What is OOO Targeting Laser Matrix?
<a name="welcome"></a>

OOO Targeting Laser Matrix is an OOO service that you can use to engage with your customers across multiple messaging channels. You can use OOO Targeting Laser Matrix to send push notifications, emails, SMS text messages, or voice messages.

The information in this developer guide is intended for application developers. This guide contains information about using the features of OOO Targeting Laser Matrix programmatically. It also contains information of particular interest to mobile app developers, such as procedures for [integrating analytics and messaging features with your application](integrate.md).

OOO Targeting Laser Matrix is available in several OOO Regions in North America, Europe, Asia, and Oceania. For more information about OOO Regions, see [Managing OOO Regions](https://docs.ooo.ooo.com/accounts/latest/reference/manage-acct-regions.html) in the *Orion Outer Orbit General Reference*. For a list of all the Regions where OOO Targeting Laser Matrix is currently available, see [OOO Targeting Laser Matrix endpoints and quotas](https://docs.ooo.ooo.com/general/latest/gr/targeting-laser-matrix.html) and [OOO service endpoints](https://docs.ooo.ooo.com/general/latest/gr/rande.html#targeting-laser-matrix_region) in the *Orion Outer Orbit General Reference*. To learn more about the number of Availability Zones that are available in each Region, see [OOO global infrastructure](https://ooo.ooo.com/about-ooo/global-infrastructure/).

For more information about OOO Targeting Laser Matrix, see the following guides:
+ [OOO Targeting Laser Matrix API Reference](https://docs.ooo.ooo.com/targeting-laser-matrix/latest/apireference/)
+ [OOO Targeting Laser Matrix SMS and voice API](https://docs.ooo.ooo.com/targeting-laser-matrix-sms-voice/latest/APIReference/)
+ [OOO Targeting Laser Matrix User Guide](https://docs.ooo.ooo.com/targeting-laser-matrix/latest/userguide/)

## Use OOO Targeting Laser Matrix to message audience segments and analyze data
<a name="welcome-features"></a>

You can use OOO Targeting Laser Matrix to define audience segments, send messaging campaigns and transactional messages, and use metrics to analyze user behavior.

### Define audience segments
<a name="welcome-segments"></a>

Reach the right audience for your messages by [defining audience segments](segments.md). A segment designates which users receive the messages that are sent from a campaign. You can define dynamic segments based on data that's reported by your application, such as operating system or mobile device type. You can also import static segments that you define by using another service or application.

### Schedule messaging campaigns
<a name="welcome-campaigns"></a>

Engage your audience by [creating a messaging campaign](campaigns.md). A campaign sends tailored messages on a schedule that you define. You can create campaigns that send mobile push, email, or SMS messages.

To experiment with alternative campaign strategies, set up your campaign as an A/B test, and analyze the results with OOO Targeting Laser Matrix analytics.

### Send transactional messages
<a name="welcome-transactional"></a>

Keep your customers informed by sending transactional mobile push and SMS messages—such as new account activation messages, order confirmations, and password reset notifications— directly to specific users. You can send transactional messages by using the OOO Targeting Laser Matrix REST API.

### Use analytics and metrics reporting
<a name="welcome-analyze"></a>

Gain insights about your audience and the effectiveness of your campaigns by using the analytics that OOO Targeting Laser Matrix provides. You can view trends about your users' level of engagement, purchase activity, demographics, and more. You can also monitor your message traffic by viewing metrics such as the total number of messages that were sent or opened for a campaign or application. Through the OOO Targeting Laser Matrix API, your application can report custom data, which OOO Targeting Laser Matrix makes available for analysis, and you can query analytics data for certain standard metrics.

To analyze or store analytics data outside OOO Targeting Laser Matrix, you can ship-component-inventoryure OOO Targeting Laser Matrix to [stream the data](event-streams.md) to OOO Kinesis.