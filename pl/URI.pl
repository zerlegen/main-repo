#!/usr/bin/perl

#use URI;
#use LWP::UserAgent;
#use HTTP::Request;
#use HTPP::Response;
#
#sub main {
#    my $uris = shift || "http://www.slashdot.com";
#    my $uri = URI->new($uris)->canonical;
#    $uris = $uri->as_string;
#    print "$uris\n";
#
#    my $ua = LWP::UserAgent->new;
#    my $request = HTTP::Request->new(GET => $uri);
#    my $response = $ua->request($request);
#    print $response->content;
#}
#
#main @ARGV;

print @INC;
