# Using Puppet, install `puppet-lint`.
package { 'puppet-lint':
  ensure   => '2.3.6',
  provider => 'gem',
}
