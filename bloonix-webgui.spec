Summary: Bloonix WebGUI
Name: bloonix-webgui
Version: 0.124
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-webgui-core >= 0.16
Requires: bloonix-core >= 0.41
AutoReqProv: no

%description
This is the web application of Bloonix.

%define with_systemd 0
%define srvdir /srv/bloonix/webgui

%prep
%setup -q -n %{name}-%{version}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{srvdir}
cp -a bin %{buildroot}%{srvdir}/
cp -a ChangeLog %{buildroot}%{srvdir}/
cp -a lang %{buildroot}%{srvdir}/
cp -a lib %{buildroot}%{srvdir}/
cp -a LICENSE %{buildroot}%{srvdir}/
cp -a public %{buildroot}%{srvdir}/
cp -a schema %{buildroot}%{srvdir}/
cp -a scripts %{buildroot}%{srvdir}/
cp -a templates %{buildroot}%{srvdir}/

%pre
if [ -h "/srv/bloonix/webgui" ] ; then
    rm -f /srv/bloonix/webgui
fi

%post
/srv/bloonix/webgui/bin/fix-perms

%if %{?with_systemd}
systemctl condrestart bloonix-webgui.service
%else
/sbin/service bloonix-webgui condrestart &>/dev/null
%endif

%clean
rm -rf %{buildroot}

%files
%dir %attr(0755, root, root) %{srvdir}
%defattr (-, root, root)
%{srvdir}/*

%changelog
* Mon Apr 10 2017 Jonny Schulz <js@bloonix.de> - 0.124-1
- Fixed screen bug.
* Mon Apr 10 2017 Jonny Schulz <js@bloonix.de> - 0.123-1
- Implemented checkIfElementMatchText for web transactions.
- Further utf8 fixes for all strings which are stored as
  utf8 in the database.
* Wed Mar 29 2017 Jonny Schulz <js@bloonix.de> - 0.123-1
- Implemented checkIfElementMatchText for web transactions.
* Wed Mar 08 2017 Jonny Schulz <js@bloonix.de> - 0.122-1
- Fixed umlaut issues (utf8) on the dashboard.
* Wed Jan 25 2017 Jonny Schulz <js@bloonix.de> - 0.121-1
- Fixed stacked area charts with negative values.
* Mon Jan 02 2017 Jonny Schulz <js@bloonix.de> - 0.120-1
- Implemented port number for satellites.
* Tue Dec 20 2016 Jonny Schulz <js@bloonix.de> - 0.119-1
- Fixed documentation to global check timeout for the bloonix agent.
* Thu Nov 24 2016 Jonny Schulz <js@bloonix.de> - 0.118-1
- Fixed duplicate entries for host and service intervals.
* Wed Sep 21 2016 Jonny Schulz <js@bloonix.de> - 0.117-1
- Fixed: drop selected hosts if the registration was successful.
* Mon Sep 05 2016 Jonny Schulz <js@bloonix.de> - 0.116-1
- Changed param --force to --run in quick-install.
- Fixed notification screen: OK boxes are now shows.
* Wed Aug 31 2016 Jonny Schulz <js@bloonix.de> - 0.115-1
- Created schema/quick-install for Ansible/Saltstack/... rockstars.
* Mon Aug 29 2016 Jonny Schulz <js@bloonix.de> - 0.114-1
- Implemented the new feature to hide acknowledged services
  from the notification screen.
* Mon Aug 29 2016 Jonny Schulz <js@bloonix.de> - 0.113-1
- Fixed: the notification screen now shows only services that
  are affected by the status.
* Thu Aug 18 2016 Jonny Schulz <js@bloonix.de> - 0.112-1
- Fixed bug in username selection in group->user->members.
* Thu Aug 18 2016 Jonny Schulz <js@bloonix.de> - 0.111-1
- Fixed red marked select fields.
* Fri Aug 12 2016 Jonny Schulz <js@bloonix.de> - 0.110-1
- Fixed nfs4 chart "file operations".
* Fri Aug 12 2016 Jonny Schulz <js@bloonix.de> - 0.109-1
- Increased max_result_window to 1000000 by default.
* Tue Aug 09 2016 Jonny Schulz <js@bloonix.de> - 0.108-1
- Fixed css select height.
* Tue Aug 09 2016 Jonny Schulz <js@bloonix.de> - 0.107-1
- Replaced bloonix own select-boxes with html select.
- Added field comment to the service table.
* Thu Jul 07 2016 Jonny Schulz <js@bloonix.de> - 0.106-1
- Fixed info text for notification_interval in the host form.
- The default value for service -> notification_interval is now 0.
* Thu Jul 07 2016 Jonny Schulz <js@bloonix.de> - 0.105-1
- Fixed: services from a template cannot be updated any more
  over the route /host/services.
- Fixed: added missing parameter notification_interval in the
  host form.
* Sun May 22 2016 Jonny Schulz <js@bloonix.de> - 0.104-1
- Fixed retry_interval.
* Sun May 22 2016 Jonny Schulz <js@bloonix.de> - 0.103-1
- Implemented parameter sendmail for section email.
* Thu May 19 2016 Jonny Schulz <js@bloonix.de> - 0.102-1
- Fixed tooltip feature for multiple charts.
* Wed May 18 2016 Jonny Schulz <js@bloonix.de> - 0.101-1
- Fixed the webgui slider and add the checked value
  as options if it doesn't exist.
- Decreased the min timeout for check_frequency high
  to 60 seconds.
* Wed May 18 2016 Jonny Schulz <js@bloonix.de> - 0.100-1
- Fixed tooltip z-index for icons in tables.
- Added check frequency sleepy.
* Thu May 12 2016 Jonny Schulz <js@bloonix.de> - 0.99-1
- Update to Highcharts and Highmaps 4.2.4.
- Fixed the event query search.
* Wed Apr 27 2016 Jonny Schulz <js@bloonix.de> - 0.98-1
- Kicked SLA restriction for location checks.
* Sun Apr 24 2016 Jonny Schulz <js@bloonix.de> - 0.97-1
- Changed min timeout for mid frequency to 120s.
* Tue Apr 19 2016 Jonny Schulz <js@bloonix.de> - 0.96-1
- Changed min timeout for mid frequency to 60s.
* Tue Apr 19 2016 Jonny Schulz <js@bloonix.de> - 0.95-1
- Fixed: it's not possible any more to create a location check
  with less than 2 locations.
* Thu Apr 14 2016 Jonny Schulz <js@bloonix.de> - 0.94-1
- Implemented new wtrm action doAddCookie.
* Thu Apr 14 2016 Jonny Schulz <js@bloonix.de> - 0.93-1
- Fixed the html view of the wtrm workflow.
- Fixed the call of /services/:id.
* Mon Apr 04 2016 Jonny Schulz <js@bloonix.de> - 0.91-1
- Fixed description of max_sms.
* Thu Mar 31 2016 Jonny Schulz <js@bloonix.de> - 0.89-1
- Bugfix: the count of max_services is now calculated correclty
  if a services is created in a template.
* Thu Mar 31 2016 Jonny Schulz <js@bloonix.de> - 0.88-1
- Implemented support for Elasticsearch index aliases.
* Wed Mar 30 2016 Jonny Schulz <js@bloonix.de> - 0.87-1
- Fixed ES dynamic mapping.
* Wed Mar 30 2016 Jonny Schulz <js@bloonix.de> - 0.86-1
- Fixed ES mapping for type event.
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.85-1
- Updated ES template for version 2.x.
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.84-1
- Fixed auto increment fields for different tables.
* Tue Mar 29 2016 Jonny Schulz <js@bloonix.de> - 0.83-1
- Splittet the MySQL schema into small files.
* Mon Mar 21 2016 Jonny Schulz <js@bloonix.de> - 0.82-1
- Delete location: list hosts and services which have the
  location configured.
* Sun Mar 20 2016 Jonny Schulz <js@bloonix.de> - 0.81-1
- Improved transaction handling.
- New column table service: agent_dead
* Fri Feb 12 2016 Jonny Schulz <js@bloonix.de> - 0.80-1
- Kicked field "authkey" for locations. The database column
  will be dropped.
- Some italian lang fixes.
* Tue Feb 09 2016 Jonny Schulz <js@bloonix.de> - 0.79-1
- Added lang italiana.
* Wed Nov 25 2015 Jonny Schulz <js@bloonix.de> - 0.78-1
- Fixed dashboard resizing.
- Disallow host registrations for company id 1.
* Wed Nov 25 2015 Jonny Schulz <js@bloonix.de> - 0.77-1
- Fixed access to hosts/registered/count for role user.
* Wed Nov 25 2015 Jonny Schulz <js@bloonix.de> - 0.76-1
- Fixed content type and output for routes /operateas and /logout.
* Sat Nov 21 2015 Jonny Schulz <js@bloonix.de> - 0.75-1
- Change: Field "description" of hosts is now an optional parameter.
- New Feature: It's now possible to configure the authkey for each
  location in the webgui.
- Kicked deprecated host parameters: hw_manufacturer, hw_product
  os_manufacturer, os_product, virt_manufacturer,j virt_product,
  location.
- Implemented Bloonix::NetAddr to change IP ranges.
- Implemented the feature to set bloonix into maintenance.
* Wed Nov 18 2015 Jonny Schulz <js@bloonix.de> - 0.75-1
- Change: Field "description" of hosts is now an optional parameter.
- New Feature: It's now possible to configure the authkey for each
  location in the webgui.
- Kicked deprecated host parameters: hw_manufacturer, hw_product
  os_manufacturer, os_product, virt_manufacturer,j virt_product,
  location.
- Implemented Bloonix::NetAddr to change IP ranges.
- Implemented the feature to set bloonix into maintenance..
* Fri Sep 18 2015 Jonny Schulz <js@bloonix.de> - 0.74-1
- Fixed null values in host view.
* Fri Sep 18 2015 Jonny Schulz <js@bloonix.de> - 0.73-1
- Updated host view fields.
* Fri Sep 18 2015 Jonny Schulz <js@bloonix.de> - 0.72-1
- Fixed: ipaddr6 is now a optional field.
* Fri Sep 18 2015 Jonny Schulz <js@bloonix.de> - 0.71-1
- Filter by host classes are now case sensitive.
* Thu Sep 17 2015 Jonny Schulz <js@bloonix.de> - 0.70-1
- Fixed class search if whitespaces are in the class name.
* Thu Sep 17 2015 Jonny Schulz <js@bloonix.de> - 0.69-1
- Fixed different column in table dependency and allow null values.
- Add new host columns os_class, hw_class and env_class.
* Tue Sep 08 2015 Jonny Schulz <js@bloonix.de> - 0.68-1
- Improved the order for host lists, so that hosts that were not OK
  in the last 60 minutes are displayed before all other hosts.
- Fixed duplicate pager at the bottom of some tables.
- Fixed host form, so that only groups are selectable in which
  the user is a member.
- Sort services by service name in templates.
- Fixed different column in table dependency and allow null values.
- Add new host columns os_class, hw_class and env_class.
* Mon Sep 07 2015 Jonny Schulz <js@bloonix.de> - 0.67-1
- Kicked default Host classes.
- Added the possibility to configure the monitoring screen.
* Sun Sep 06 2015 Jonny Schulz <js@bloonix.de> - 0.66-1
- Increased chart alignment from 3 to 8.
- Added route /administration/hosts/$id.
- Fixed the issue that services in templates couldn't be deleted.
- A lightning icon will be displayed if a host or service was not
  OK within the last 60 minutes.
- Fixed link and text of sysinfo.
- Renamed device_class to host_class.
- Implemented system_class and location_class.
* Tue Sep 01 2015 Jonny Schulz <js@bloonix.de> - 0.65-1
- Fixed Elasticsearch template: dynamic_templates includes now
  double, float, long and integer.
- The Elasticsearch template is now updated automatically.
* Mon Aug 31 2015 Jonny Schulz <js@bloonix.de> - 0.64-1
- The description field of host template can now be empty.
- Max attempts can be set to 0 to disable notifications.
* Mon Aug 24 2015 Jonny Schulz <js@bloonix.de> - 0.63-1
- Fixed: result data are not empty any more.
* Sun Aug 23 2015 Jonny Schulz <js@bloonix.de> - 0.62-1
- If the parameter is_demo is set to true and if the logged in user called "demo",
  then the user has no permissions to call create|update|delete|add|remove actions.
- Fixed viewing advanced service data.
* Thu Aug 20 2015 Jonny Schulz <js@bloonix.de> - 0.61-1
- Kicked '#' from the string list for the password generation in
  init-database.sh
- Fixed double creation of table lock_srvchk.
* Sat Aug 15 2015 Jonny Schulz <js@bloonix.de> - 0.60-1
- Fixed alter/rename syntax for mysql upgrade.
* Thu Aug 06 2015 Jonny Schulz <js@bloonix.de> - 0.58-1
- Heavy changes in the schema of bloonix and re-designed
  the notification handling.
* Wed Jun 24 2015 Jonny Schulz <js@bloonix.de> - 0.57-1
- Added new WTRM features: doSwitchToNewPage and doSwitchToMainPage.
* Mon Jun 22 2015 Jonny Schulz <js@bloonix.de> - 0.56-1
- Added new WTRM features: doTriggerEvent, doSwitchToFrame,
  doSwitchToParentFrame, doDumpContent and doDumpFrameContent.
* Sat Jun 20 2015 Jonny Schulz <js@bloonix.de> - 0.55-1
- Fixed service chart creation on the dashboard.
* Sat Jun 20 2015 Jonny Schulz <js@bloonix.de> - 0.54-1
- Improved random string generation in sha256 and sha512.
* Sat Jun 20 2015 Jonny Schulz <js@bloonix.de> - 0.53-1
- The sub navigations of administration/groups and contactgroups
  was hidden.
* Wed Jun 17 2015 Jonny Schulz <js@bloonix.de> - 0.52-1
- Added new feature to the dashboard to show or hide the legend
  of charts.
* Wed Jun 17 2015 Jonny Schulz <js@bloonix.de> - 0.51-1
- Kicked vertical navigation.
- Fixed background color of body.
* Mon Jun 15 2015 Jonny Schulz <js@bloonix.de> - 0.50-1
- Fixed "CASCADE NULL" in schema-pg.sql.
* Wed Jun 10 2015 Jonny Schulz <js@bloonix.de> - 0.49-1
- Fixed the error handling of the login page.
- Fixed font-weight in the top navigation.
- Implemnted a data retention as company param that has
  a higher priority as the data retention of a host.
- Fixed column variables of company for company id 1.
* Mon Jun 01 2015 Jonny Schulz <js@bloonix.de> - 0.48-1
- Default font-weight set to normal.
* Mon Jun 01 2015 Jonny Schulz <js@bloonix.de> - 0.47-1
- Implemented a small workaround for a bug in check-by-satellite
  of bloonix-plugins-basic 0.37.
- Created a new style.
- Changed the default font to "Open Sans" and added a info to
  the license file.
* Thu May 14 2015 Jonny Schulz <js@bloonix.de> - 0.46-1
- Fixed/added transactions support for mysql.
* Thu May 14 2015 Jonny Schulz <js@bloonix.de> - 0.45-1
- Quick fix for init-database.
* Thu May 07 2015 Jonny Schulz <js@bloonix.de> - 0.44-1
- Added support for MySQL.
- Sort thresholds in service form.
* Thu Apr 23 2015 Jonny Schulz <js@bloonix.de> - 0.43-1
- Improved service parameter parsing.
* Mon Apr 20 2015 Jonny Schulz <js@bloonix.de> - 0.42-1
- Fixed bug: drop column country_code only if the column exist - 2.
* Mon Apr 20 2015 Jonny Schulz <js@bloonix.de> - 0.41-1
- Fixed bug: drop column country_code only if the column exist.
* Sun Apr 19 2015 Jonny Schulz <js@bloonix.de> - 0.40-1
- Fixed bug: if a template is added to a host then max_services=0 is not
  treated as unlimited.
* Sun Apr 19 2015 Jonny Schulz <js@bloonix.de> - 0.39-1
- Kicked parameter show_locations and make the location feature available.
* Fri Apr 17 2015 Jonny Schulz <js@bloonix.de> - 0.38-1
- Fixed version number handling in database maintenance.
* Thu Apr 16 2015 Jonny Schulz <js@bloonix.de> - 0.37-1
- Bloonix Satellite implemented.
* Sun Apr 05 2015 Jonny Schulz <js@bloonix.de> - 0.36-1
- Limits implemented.
* Fri Mar 13 2015 Jonny Schulz <js@bloonix.de> - 0.35-1
- Fixed column creation for the service table.
* Wed Mar 11 2015 Jonny Schulz <js@bloonix.de> - 0.34-1
- Added column data_retention to table host.
* Tue Mar 10 2015 Jonny Schulz <js@bloonix.de> - 0.33-1
- Modified ES template and force object some keys to type 'string'.
- Fixed building of location option for templates.
- Show the inherited time values for timeouts and intervals for services.
- Moved the submit button to create user charts into the overlay footer.
- Added column volatile_comment to table service.
- Now all actions (acknowlegded, notification, active, volatile) will be logged.
* Mon Feb 16 2015 Jonny Schulz <js@bloonix.de> - 0.32-1
- Improved the database upgrade.
- Migrate dashboard width from 9 to 12 and height from 6 to 12.
- Changed the order of dashlet icons and fixed the initial dashlet
  width and height
- Pattern fixed in init-database.
* Sun Feb 15 2015 Jonny Schulz <js@bloonix.de> - 0.31-1
- Fixed quoting of init-database.
* Sat Feb 14 2015 Jonny Schulz <js@bloonix.de> - 0.30-1
- Scale dashlets on the dashboard to a value related to the content width.
- Init-database now replaces the pattern @@PASSWORD@@ in the configuration.
* Thu Feb 12 2015 Jonny Schulz <js@bloonix.de> - 0.29-1
- New feature: doWaitForElement can now wait for text within an element too.
* Thu Feb 12 2015 Jonny Schulz <js@bloonix.de> - 0.28-1
- Fixed typo safe -> save.
- Fixed empty variable handling (agent_options).
* Mon Jan 26 2015 Jonny Schulz <js@bloonix.de> - 0.27-1
- Fixed <br/> in dependency table.
- Hide nav item "company" if the user is not an admin.
- Kicked parameter company_id for contact forms.
- Replaced the raw call /usr/sbin/sendmail with MIME::Lite.
* Tue Jan 20 2015 Jonny Schulz <js@bloonix.de> - 0.26-1
- Fix installation.
* Sun Jan 18 2015 Jonny Schulz <js@bloonix.de> - 0.25-1
- Make it unpossible to delete user and group with id 1.
