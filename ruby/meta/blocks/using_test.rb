require 'using'
require 'test/unit'

class TestUsing < Test::Unit::TestCase
    class Resource
	def dispose
	    @dispose = true
	end

	def disposed?
	    @disposed
	end
    end
    def test_dispose_of_resource
	r = Resource.new
	using(r) {}
	assert r.disposed?
    end

    def test_dispose_of_resources_in_case_of_exception
	r = Resource.new
	assert_raises(Exception) {
	    using(r) {
		raise Exception
	    }
	}
    end
end
